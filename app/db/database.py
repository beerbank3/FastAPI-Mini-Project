from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import redis
# PostgreSQL 데이터베이스 연결 정보
DATABASE_URL = "postgresql://postgres:root@postgres:5432/developer"

# SQLAlchemy 엔진 및 세션 설정
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

redis_client = redis.Redis(host="redis", port=6379, db=0)

# FastAPI 의존성으로 세션 제공
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()