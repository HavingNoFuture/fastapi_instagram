from fastapi import FastAPI

from app.auth import services
from app.auth.schemas import UserSignUpPostData, UserSignUpViewData

auth = FastAPI()


@auth.post("/signup", status_code=201, response_model=UserSignUpViewData)
async def signup(user_data: UserSignUpPostData):
    """
    Регистрация пользователя
    """
    return await services.create_user(user_data)
