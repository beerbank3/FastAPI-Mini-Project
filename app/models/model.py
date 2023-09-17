from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base,engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # User 클래스와 Board 클래스 사이의 관계 설정
    boards = relationship("Board", back_populates="owner")
    posts = relationship("Post", back_populates="owner")

class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    public = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Board 클래스와 User 클래스 사이의 관계 설정
    owner = relationship("User", back_populates="boards")
    posts = relationship("Post", back_populates="board")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    board_id = Column(Integer, ForeignKey("boards.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Post 클래스와 Board 클래스, User 클래스 사이의 관계 설정
    board = relationship("Board", back_populates="posts")
    owner = relationship("User", back_populates="posts")

Base.metadata.create_all(bind=engine)