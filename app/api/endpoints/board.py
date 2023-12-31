from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models.model import User
from app.db.database import get_db
from app.schemas.board import Board, BoardCreate, BoardUpdate, BoardDelete
from app.crud.crud_board import CRUDBoard
from app.core.security import api_key_header, get_current_user
router = APIRouter()

def user_token_authenticate(token):
    user = get_current_user(token)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return int(user)

@router.post("/create/", response_model=BoardCreate)
def create_board(board: BoardCreate, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token)
    return CRUDBoard.create_board(db, board=board, owner_id=owner_id)

@router.post("/update/", response_model=BoardUpdate)
def update_board(board: BoardUpdate, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token)
    db_board = CRUDBoard.get_board(db, board.id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != owner_id:
        raise HTTPException(status_code=403, detail="Permission denied")
    return CRUDBoard.update_board(db, board.id, board)

@router.post("/delete/", response_model=Board)
def delete_board(board: BoardDelete, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token)
    db_board = CRUDBoard.get_board(db, board.id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != owner_id:
        raise HTTPException(status_code=403, detail="Permission denied")
    
    delete_board = CRUDBoard.delete_board(db, board.id)
    if not delete_board:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Board deleted successfully"}


@router.get("/{board_id}/", response_model=Board)
def get_board(board_id: int, db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token)
    db_board = CRUDBoard.get_board(db, board_id)
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    if db_board.owner_id != owner_id and not db_board.public:
        raise HTTPException(status_code=403, detail="Permission denied")
    
    return CRUDBoard.get_board(db, board_id)


@router.get("/")
def read_board(skip: int,db: Session = Depends(get_db), token: str = Depends(api_key_header)):
    owner_id = user_token_authenticate(token)
    if not skip:
        skip = 0
    return CRUDBoard.list_boards(db, owner_id,skip)