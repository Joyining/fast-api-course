from fastapi import FastAPI
from . import schemas, models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post('/blog')
def create_blog(blog: schemas.Blog):
    return 'A blog was created.'
