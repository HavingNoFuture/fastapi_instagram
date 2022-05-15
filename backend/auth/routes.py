from fastapi import APIRouter, HTTPException, status

from backend.auth import services
from backend.auth.schemas import UserSignUpPostData, UserSignUpViewData

auth_router = APIRouter()


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserSignUpViewData)
async def signup(user_data: UserSignUpPostData):
    """
    Регистрация пользователя
    """
    user_data = await services.create_user(user_data)
    if 'error' in user_data:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=user_data.get('error'))
    return user_data
