from fastapi import FastAPI

from app.users.schemas import UserRegistration, UserBase

users_api = FastAPI()


@users_api.post("/registration", response_model=UserBase)
async def user_registration(user: UserRegistration):
    return user
