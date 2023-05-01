from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from typing import List

router = APIRouter()


@router.post('/blogs', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create_blog(blog: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(
        title=blog.title,
        body=blog.body,
        user_id=1  # FIXME: Temporarily hard code user_id to 1.
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.delete
@router.delete('/blogs/{blog_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete_blog(blog_id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==
                                        blog_id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} is not available.')
    db.commit()
    return 'deleted.'


@router.get('/blogs', response_model=List[schemas.ShowBlog], tags=['blogs'])
def get_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get('/blogs/{blog_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['blogs'])
def get_blog(blog_id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} is not available.')
    return blog


# https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.update
@router.put('/blogs/{blog_id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update_blog(blog_id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} is not available.')
    blog.update(request.dict())
    db.commit()
    return 'updated.'
