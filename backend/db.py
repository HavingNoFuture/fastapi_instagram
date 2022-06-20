import typing
from contextlib import contextmanager

from databases import Database
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from config import settings

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
database = Database(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()


def get_db() -> Session:
    """
    Получение сессии БД + гарантированное ее закрытие
    todo: Выпилить
    :return: Session
    """
    try:
        db = sessionmaker(bind=engine)()
        yield db
    finally:
        db.close()


@contextmanager
def db_session(**kwargs) -> typing.ContextManager[Session]:
    """Контекстный менеджер для сессии БД"""
    session_kwargs = {'autocommit': False, 'autoflush': False}
    session_kwargs.update(kwargs)
    new_session = sessionmaker(bind=engine, **session_kwargs)()
    try:
        yield new_session
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()


def model_to_dict(obj) -> dict:
    """
    Преобразует объект SQLAlchemy модели в питоновский dict
    :param obj: Объект SQLAlchemy модели
    :return: Словарь со столбцами объекта
    # todo: Поискать решение как возвращать из рута объект модели
    """
    return {column.key: getattr(obj, column.key) for column in inspect(obj).mapper.column_attrs}
