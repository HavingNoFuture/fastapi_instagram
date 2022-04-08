from pydantic import BaseModel, Field, EmailStr


class UserRegistration(BaseModel):
    """
    Схема регистрации пользователя
    """

    login: str = Field(..., title="Логин пользователя")
    email: EmailStr = Field(..., title="Email пользователя")
    password: str = Field(..., title="Пароль пользователя")
