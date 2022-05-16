from fastapi import FastAPI

from backend.auth.routes import auth
from backend.posts.routes import posts_router

app = FastAPI()


app.mount("/auth", auth)
app.include_router(posts_router, prefix='/posts')
