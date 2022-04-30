from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Базовая схема пользователя"""

    email: EmailStr = Field(..., title="Email пользователя")


class UserSignUpPostData(UserBase):
    """Схема пользователя запрвшиваемая при регистрации"""

    password: str = Field(..., title="Пароль пользователя")


class UserSignUpViewData(UserBase):
    """Схема пользователя возвращаемая при регистрации"""

    id: int = Field(..., title="ID пользователя")
