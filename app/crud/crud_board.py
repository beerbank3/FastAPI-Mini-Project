from sqlalchemy.orm import Session
from app.schemas.board import BoardCreate, BoardUpdate
from app.models.model import Board, Post
from sqlalchemy import and_, or_, func

class CRUDBoard:

    def create_board(db: Session, board: BoardCreate, owner_id: int):
        db_board = Board(**board.dict(), owner_id=owner_id)
        db.add(db_board)
        db.commit()
        db.refresh(db_board)
        return db_board

    def update_board(db: Session, board_id: int, board: BoardUpdate):
        db_board = db.query(Board).filter(Board.id == board_id).first()
        if db_board:
            for key, value in board.dict().items():
                setattr(db_board, key, value)
            db.commit()
            db.refresh(db_board)
        return db_board

    def delete_board(db: Session, board_id: int):
        db_board = db.query(Board).filter(Board.id == board_id).first()
        if db_board:
            db.delete(db_board)
            db.commit()
            return db_board

    def get_board(db: Session, board_id: int):
        return db.query(Board).filter(Board.id == board_id).first()

    def list_boards(db: Session, owner_id: int, skip: int, limit: int = 10):
        subquery = (
            db.query(Post.board_id, func.count(Post.id).label('post_count'))
            .group_by(Post.board_id)
            .subquery()
        )
        filter_condition = or_(Board.public == True, Board.owner_id == owner_id)
        return db.query(Board).outerjoin(subquery, Board.id == subquery.c.board_id).filter(filter_condition).order_by(func.coalesce(subquery.c.post_count, 0).desc()).offset(skip).limit(limit).all()