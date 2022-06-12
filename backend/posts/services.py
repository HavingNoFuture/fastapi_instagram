from sqlalchemy.orm import Session

from core.services import BaseServices, ModelType

from .models import Comment, Post
from .schemas import CommentCreate, CommentUpdate, PostCreate, PostUpdate


class PostServices(BaseServices[Post, PostCreate, PostUpdate]):
    """
    Действия с публикациями
    """

    async def post_list_by_user(
        self,
        db: Session,
        user_id: int,
    ) -> list[ModelType]:
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
    ) -> list[ModelType]:
        """
        Список комментариев к посту
        """
        return db.query(self.model).filter(self.model.post == post_id).all()


comment = CommentServices(Comment)
