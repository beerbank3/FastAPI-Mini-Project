from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models.model import User
from app.db.database import get_db
from app.schemas.user import UserLogin
from app.crud.crud_user import CRUDUser
from app.core.security import create_access_token
import app.schemas.token as schemas
from app.core.security import api_key_header, delete_token

router = APIRouter()

@router.post("/login/", response_model=schemas.Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    db_user = CRUDUser.authenticate(db,email=user_login.email, password=user_login.password)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(db_user.id)
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout/")
def logout(token: str = Depends(api_key_header)):
    delete_token(token)
    return {"message":"로그아웃"}