from fastapi import FastAPI

from backend.auth.routes import auth

app = FastAPI()


app.mount("/auth", auth)
