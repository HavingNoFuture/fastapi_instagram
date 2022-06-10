from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Настройки приложения
    """

    SQLALCHEMY_DATABASE_URL: str = ''


settings = Settings('.env')  # Файл с переменными окружения должен лежать в корне проекта (вне '/backend/')
# todo: Разобраться с относительными импортами. В идеале засунуть все в докер
