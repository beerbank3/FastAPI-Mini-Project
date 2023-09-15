from fastapi import FastAPI
from api.api import api_router
from db.database import Base, engine


app = FastAPI()

app.include_router(api_router)
Base.metadata.create_all(bind=engine)

