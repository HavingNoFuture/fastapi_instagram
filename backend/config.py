from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Настройки приложения
    """

    SQLALCHEMY_DATABASE_URL: str = ''


settings = Settings()
