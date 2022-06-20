from fastapi import APIRouter, status
from fastapi.security import HTTPBasic

from auth.schemas import UserSignInPostData, UserSignUpPostData, UserSignUpViewData
from auth.services import AuthService
from db import model_to_dict

auth_router = APIRouter()

security = HTTPBasic()


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserSignUpViewData)
def signup(user_data: UserSignUpPostData):
    """
    Регистрация пользователя
    """
    return model_to_dict(AuthService.create_user(user_data))


@auth_router.post("/signin", status_code=status.HTTP_201_CREATED, response_model=UserSignUpViewData)
def signin(user_data: UserSignInPostData):
    """
    Логин пользователя
    """
    return model_to_dict(AuthService.authenticate_user(user_data))
