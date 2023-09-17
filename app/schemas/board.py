from pydantic import BaseModel

class BoardBase(BaseModel):
    name: str
    public: bool

class BoardCreate(BoardBase):
    pass

class BoardUpdate(BoardBase):
    id: int
    name: str
    public: bool


class BoardDelete(BaseModel):
    id: int

    
class Board(BoardBase):
    id: int

    class Config:
        from_attributes = True