from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from .models import Post, Comment
from .schemas import PostCreate, PostUpdate, CommentCreate, CommentUpdate
from ..core.services import BaseServices, ModelType


class PostServices(BaseServices[Post, PostCreate, PostUpdate]):
    """
    Действия с публикациями
    """

    async def post_list_by_user(
        self,
        db: Session,
        user_id: int,
    ) -> List[ModelType]:
        return db.query(self.model).filter(self.model.user == user_id).all()


post = PostServices(Post)


class CommentServices(BaseServices[Comment, CommentCreate, CommentUpdate]):
    """
    Действия с комментариями
    """

    async def comments_by_post(
        self,
        db: Session,
        post_id: int,
    ) -> List[ModelType]:
        """
        Список комментариев к посту
        """
        return db.query(self.model).filter(self.model.post == post_id).all()


comment = CommentServices(Comment)
