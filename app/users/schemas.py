from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    """
    Базовая схема пользователя
    """

    login: str = Field(..., title="Логин пользователя")
    email: EmailStr = Field(..., title="Email пользователя")


class UserRegistration(UserBase):
    """
    Схема регистрации пользователя
    """

    password: str = Field(..., title="Пароль пользователя")
