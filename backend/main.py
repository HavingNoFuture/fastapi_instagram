from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.auth.routes import auth_router
from backend.posts.routes import posts_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix='/auth')
app.include_router(posts_router, prefix='/posts')
