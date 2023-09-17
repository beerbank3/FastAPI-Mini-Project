from fastapi import APIRouter

from app.api.endpoints import board, login, users, posts

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(board.router, prefix="/boards", tags=["board"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])