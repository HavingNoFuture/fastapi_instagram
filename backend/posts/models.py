from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from db import Base


class Post(Base):
    """
    Модель Публикации
    """

    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(350))
    image = Column(String)
    pub_date = Column(DateTime(), server_default=now())
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship('User')


class Comment(Base):
    """
    Модель Комментария
    """

    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(350))
    pub_date = Column(DateTime(), server_default=now())
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship('User')
    post = Column(Integer, ForeignKey('post.id'))
    post_id = relationship('Post')


class Like(Base):
    """
    Модель Отметок "нравится"
    """

    __tablename__ = "like"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship('User')
    post = Column(Integer, ForeignKey('post.id'))
    post_id = relationship('Post')
