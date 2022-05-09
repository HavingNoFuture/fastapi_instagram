from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql.functions import now

from backend.db import Base


class User(Base):
    """Модель пользователя"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    first_name = Column(String(75))
    last_name = Column(String(75))
    signup_date = Column(DateTime(), server_default=now())
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f'Пользователь (id={self.id!r}, email={self.email!r})'

    def __init__(self, email, password):
        self.email = email
        self.password = password
