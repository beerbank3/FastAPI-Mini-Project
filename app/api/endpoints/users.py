from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models.model import User
from app.db.database import get_db
from app.schemas.user import UserCreate
from app.crud.crud_user import CRUDUser
import app.schemas.user as schemas

router = APIRouter()

# 회원가입
@router.post("/signup/", response_model=schemas.User)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return CRUDUser.create(db, obj_in=user)