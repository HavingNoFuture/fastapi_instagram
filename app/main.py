from fastapi import FastAPI

from app.users.routers import users_api

app = FastAPI()


app.mount("/users", users_api)
