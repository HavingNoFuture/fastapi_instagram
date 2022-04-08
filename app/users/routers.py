from fastapi import FastAPI

from app.users.schemas import UserRegistration

users_api = FastAPI()


@users_api.post("/registration")
async def user_registration(user: UserRegistration):
    return user
