from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.post import Post, PostCreate, PostUpdate, PostDelete  # 새로운 스키마를 import합니다.
from app.crud.crud_post import CRUDPost  # CRUDPost 클래스를 import합니다.
from app.crud.crud_board import CRUDBoard
from app.core.security import api_key_header, get_current_user

router = APIRouter()

def user_token_authenticate(token,bool):
    user = get_current_user(token)
    if user is None and bool:
        raise HTTPException(status_code=404, detail="User not found")
    if user:
        return int(user)
    return None

# Create a new post
@router.post("/create/", response_model=PostCreate)
def create_post(post: PostCreate, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    # You may want to add authentication here to ensure that the user creating the post is allowed to
    # create posts in the specified board.
    owner_id = user_token_authenticate(token,True)

    db_board = CRUDBoard.get_board(db, post.board_id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != owner_id and not db_board.public:
        raise HTTPException(status_code=403, detail="Permission denied")
    
    return CRUDPost.create_post(db, post, owner_id)

# Update a post
@router.post("/update/", response_model=PostUpdate)
def update_post(post: PostUpdate, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token,True)
    updated_post = CRUDPost.update_post(db, post=post ,owner_id=owner_id)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

# Delete a post
@router.post("/delete/")
def delete_post(post:PostDelete, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token,True)
    deleted_post = CRUDPost.delete_post(db, post.id, owner_id=owner_id)
    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}

# Get a post by ID
@router.get("/get/{post_id}/", response_model=Post)
def get_post(post_id: int, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token,False)
    db_board = CRUDBoard.get_board(db, post_id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != owner_id and not db_board.public:
        raise HTTPException(status_code=403, detail="Permission denied")
    
    post = CRUDPost.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# List posts in a board
@router.get("/{board_id}/")
def list_posts(board_id:int, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token,True)
    db_board = CRUDBoard.get_board(db, board_id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != owner_id and not db_board.public:
        raise HTTPException(status_code=403, detail="Permission denied")

    skip = 0
    posts = CRUDPost.post_list(db,board_id=board_id,skip=skip)
    return posts
