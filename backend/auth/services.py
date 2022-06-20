from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError

from auth.models import User
from auth.schemas import UserSignInPostData, UserSignUpPostData
from db import db_session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    """
    Возвращает текущего пользователя
    """
    return AuthService.authenticate_user(credentials)


class AuthService:
    """
    Сервис авторизации пользователя
    """

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """
        Возвращает подтверждение пароля
        :param plain_password: Пароль в НЕзахешированном виде
        :param hashed_password: Пароль в захешированном виде
        :return: Соответвтсвует ли пароль хешу
        """
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        """
        Возвращает хеш пароля
        :param password: Пароль
        :return: Хеш пароля
        """
        return pwd_context.hash(password)

    @classmethod
    def create_user(cls, item: UserSignUpPostData) -> dict:
        """
        Создание пользователя в БД
        :param item: Данные пользователя для создания
        :return: Данные созданного пользователя
        """
        user_data = item.dict()
        user_data['password'] = cls.get_password_hash(user_data['password'])

        user = User(**user_data)
        try:
            with db_session() as s:
                s.add(user)
                s.commit()
                s.refresh(user)
                return user
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Пользователь уже существует!')

    @classmethod
    def authenticate_user(cls, item: UserSignInPostData | HTTPBasicCredentials) -> User:
        """
        Аутентификация пользователя
        :param item: Данные пользователя для логина
        """
        user_data = item.dict()
        with db_session() as s:
            user = s.query(User).filter(User.username == user_data['username']).first()
        if not cls.verify_password(user_data['password'], user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Некорректный логин или пароль",
                headers={"WWW-Authenticate": "Basic"},
            )
        return user
