from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from models.user import User
from db.database import get_db
from schemas.user import UserCreate
from crud.crud_user import CRUDUser
import schemas.user

router = APIRouter()

# 회원가입
@router.post("/signup/", response_model=schemas.user.User)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return CRUDUser.create(db, obj_in=user)