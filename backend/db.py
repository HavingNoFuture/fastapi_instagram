from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.config import settings

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
database = Database(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()

Session = sessionmaker(bind=engine)


def get_db() -> Session:
    """
    Получение сессии БД + гарантированное ее закрытие
    :return: Session
    """
    try:
        db = Session()
        yield db
    finally:
        db.close()
