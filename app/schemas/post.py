from pydantic import BaseModel

class Post(BaseModel):
    id: int
    title: str
    content: str
    board_id: int

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    board_id:int
    pass


class PostUpdate(PostBase):
    id: int


class PostList(BaseModel):
    board_id:int
    skip:int

class PostDelete(BaseModel):
    id: int