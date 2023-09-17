from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostUpdate
from app.models.model import Post, Board
from sqlalchemy import and_, or_

class CRUDPost:

    def create_post(db: Session, post: PostCreate, owner_id: int):
        db_post = Post(**post.dict(), owner_id=owner_id)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    def update_post(db: Session, post: PostUpdate, owner_id:int):
        filter_condition = and_(Post.id == post.id, Post.owner_id == owner_id)

        db_post = db.query(Post).filter(filter_condition).first()
        if db_post:
            for key, value in post.dict().items():
                setattr(db_post, key, value)
            db.commit()
            db.refresh(db_post)
        return db_post

    def delete_post(db: Session, post_id: int, owner_id: int):
        filter_condition = and_(Post.id == post_id, Post.owner_id == owner_id)
        
        db_post = db.query(Post).filter(filter_condition).first()
        if db_post:
            db.delete(db_post)
            db.commit()
            return db_post

    def get_post(db: Session, post_id: int):
        return db.query(Post).filter(Post.id == post_id).first()
    
    def post_list(db: Session, board_id: int, skip: int, limit: int = 10):
        return db.query(Post).filter(Post.board_id == board_id).offset(skip).limit(limit).all()