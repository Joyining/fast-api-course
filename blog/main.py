from fastapi import FastAPI
from . import models
from .database import engine, get_db
from .routers import blogs, users

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blogs.router)
app.include_router(users.router)
