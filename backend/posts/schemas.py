from datetime import datetime

from pydantic import BaseModel, Field


class PostBase(BaseModel):
    """
    Базовая схема публикации
    """

    image: str = Field(..., title="Изображение")
    text: str = Field(..., title="Текст")


class PostList(PostBase):
    """
    Схема публикации в списке
    """

    pub_date: datetime = Field(..., title="Дата публикации")

    class Config:
        orm_mode = True


class PostBaseCreateUpdate(PostBase):
    """
    Базовая Схема создания/редактирования публикации
    """

    user: int


class PostCreate(PostBaseCreateUpdate):
    """
    Схема создания публикации
    """


class PostUpdate(PostBaseCreateUpdate):
    """
    Схема редактирования публикации
    """


class PostSingle(PostBase):
    """
    Схема публикации при одиночном просмотре
    """

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    """
    Базовая схема комментариев
    """

    text: str = Field(..., title="Текст")


class CommentList(CommentBase):
    """
    Схема списка комментариев
    """

    class Config:
        orm_mode = True


class CommentBaseCreateUpdate(CommentBase):
    """
    Базовая Схема для создания/редактирования комментариев
    """

    user: int
    post: int


class CommentCreate(CommentBaseCreateUpdate):
    """
    Схема созданию комментариев
    """


class CommentUpdate(CommentBaseCreateUpdate):
    """
    Схема изменения комментариев
    """
