from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError

from backend.auth.models import User
from backend.auth.schemas import UserSignUpPostData
from backend.db import Session

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
        try:
            s.add(user)
            s.commit()
            user_data = {'id': user.id, 'email': user.email}
        except IntegrityError:
            user_data = {'error': 'Пользователь уже существует!'}
    return user_data


# endregion: User
