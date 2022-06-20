from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql.functions import now

from db import Base


class User(Base):
    """Модель пользователя"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(25), nullable=False)
    first_name = Column(String(25))
    last_name = Column(String(25))
    signup_date = Column(DateTime(), server_default=now())
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    class Config:
        orm_mode = True

    def __repr__(self):
        return f'Пользователь (id={self.id!r}, username={self.username!r})'
