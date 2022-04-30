from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.auth.models import User
from app.auth.schemas import UserSignUpPostData
from app.db import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Возвращает подтверждение пароля
    :param plain_password: Пароль в НЕзахешированном виде
    :param hashed_password: Пароль в захешированном виде
    :return: Соответвтсвует ли пароль хешу
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Возвращает хеш пароля
    :param password: Пароль
    :return: Хеш пароля
    """
    return pwd_context.hash(password)


# region: User


async def create_user(item: UserSignUpPostData) -> dict:
    """
    Создание пользователя в БД
    :param item: Данные пользователя для создания: email и пароль
    :return: Данные созданного пользователя: id и email
    """
    data = item.dict()
    data['password'] = get_password_hash(data['password'])
    with Session() as s:
        user = User(**data)
        s.add(user)
        s.commit()
        user_data = {'id': user.id, 'email': user.email}
    return user_data


# endregion: User
