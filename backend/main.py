from fastapi import FastAPI

from backend.auth.routes import auth
from backend.posts.routes import post_router

app = FastAPI()


app.mount("/auth", auth)
app.mount("/posts", post_router)
