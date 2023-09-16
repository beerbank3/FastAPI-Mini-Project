from datetime import datetime, timedelta
from typing import Any, Union
from fastapi.security import APIKeyHeader
import secrets
from jose import jwt
from passlib.context import CryptContext
from app.db.database import redis_client
from app.models.model import User
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY: str = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 3600

api_key_header = APIKeyHeader(name="Token")

def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            seconds=ACCESS_TOKEN_EXPIRE_SECONDS
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    redis_client.set(encoded_jwt, subject, ex=ACCESS_TOKEN_EXPIRE_SECONDS)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_current_user(token: str) -> User:
    user = redis_client.get(token)
    if user is None:
        return None
    return user

def delete_token(token: str) -> bool:
    deleted_count  = redis_client.delete(token)

    if deleted_count > 0:
        return True
    
    return False
