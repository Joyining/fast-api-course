from fastapi import FastAPI
from . import models
from .database import engine, get_db
from .routers import authentication, blogs, users

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)
