from fastapi import FastAPI

from app.auth.routes import auth

app = FastAPI()


app.mount("/auth", auth)
