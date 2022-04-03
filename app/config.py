import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    """
    Настройки приложения
    """

    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL")


settings = Settings()
