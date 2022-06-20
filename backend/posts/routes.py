import shutil
import uuid
from typing import Any

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND

from auth.models import User
from auth.services import get_current_user
from db import get_db
from posts import services
from posts.schemas import CommentCreate, CommentList, PostCreate, PostList, PostSingle

posts_router = APIRouter()


@posts_router.get('/user/{user_id}', response_model=list[PostList])
async def post_list_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Список публикаций
    """
    posts = await services.post.post_list_by_user(db=db, user_id=user_id)
    if not posts:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Записи не найдены')
    return posts


@posts_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_post(
    *,
    img: UploadFile = File(...),
    db: Session = Depends(get_db),
    text: str = Form(...),
    user: User = Depends(get_current_user),
):
    # async def create_post(*, img: UploadFile = File(...), db: Session = Depends(get_db), post_in: PostCreate):
    """
    Создание публикации
    """
    url = str('media/' + f'{uuid.uuid4()}{img.filename}')
    try:
        with open(url, "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)
    finally:
        img.file.close()
    post_in = PostCreate(text=text, image=url, user=user.id)
    return await services.post.create(db=db, obj_in=post_in)


@posts_router.get('/{id}', response_model=PostSingle)
async def get_post(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Получение публикации
    """
    item = services.post.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Запись не найдена')
    return item


@posts_router.get('/{post_id}/comments', response_model=list[CommentList])
async def comment_list_by_post(post_id: int, db: Session = Depends(get_db)):
    """
    Список публикаций
    """
    comments = await services.comment.comments_by_post(db=db, post_id=post_id)
    if not comments:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Комментарии не найдены')
    return comments


@posts_router.post('/{post_id}/comments/create', status_code=status.HTTP_201_CREATED)
async def create_comment(
    *, db: Session = Depends(get_db), user: User = Depends(get_current_user), comment_in: CommentCreate, post_id: int
):
    """
    Создание комментария
    """
    # todo: Добавить прокидывание текущего пользователя
    comment_in.post = post_id
    return await services.comment.create(db=db, obj_in=comment_in)
