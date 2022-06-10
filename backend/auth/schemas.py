from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Базовая схема пользователя"""

    username: str = Field(..., title="Логин пользователя")


class UserEmail(BaseModel):
    """Схема пользователя с email"""

    email: EmailStr = Field(..., title="Email пользователя")


class UserSignInPostData(UserBase):
    """Схема пользователя запрашиваемая при логине"""

    password: str = Field(..., title="Пароль пользователя")


class UserSignUpPostData(UserEmail, UserSignInPostData):
    """Схема пользователя запрашиваемая при регистрации"""


class UserSignUpViewData(UserEmail, UserBase):
    """Схема пользователя возвращаемая при регистрации"""

    id: int = Field(..., title="ID пользователя")
