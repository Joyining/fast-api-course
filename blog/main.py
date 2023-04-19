from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blogs', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=blog.title,
        body=blog.body
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.delete
@app.delete('/blogs/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==
                                        blog_id).delete(synchronize_session=False)
    db.commit()
    return 'deleted.'


@app.get('/blogs')
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blogs/{blog_id}')
def get_blog(blog_id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} is not available.')
    return blog
