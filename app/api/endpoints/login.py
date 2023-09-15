from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from models.user import User
from db.database import get_db
from schemas.user import UserLogin
from crud.crud_user import CRUDUser
from core.security import create_access_token
import schemas.token

router = APIRouter()

@router.post("/login/", response_model=schemas.token.Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    print(user_login)
    db_user = CRUDUser.authenticate(db,email=user_login.email, password=user_login.password)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(db_user.email)
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout/", status_code=status.HTTP_204_NO_CONTENT)
def logout():
    
    pass