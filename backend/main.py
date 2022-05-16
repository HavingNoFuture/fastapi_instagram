from fastapi import FastAPI

from backend.auth.routes import auth
from backend.post.routes import post_router

app = FastAPI()


app.mount("/auth", auth)
app.mount("/post", post_router)
