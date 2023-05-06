from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: schemas.BlogRequest, db: Session):
    new_blog = models.Blog(
        title=blog.title,
        body=blog.body,
        user_id=1  # FIXME: Temporarily hard code user_id to 1.
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(blog_id,  db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==
                                        blog_id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} is not available.')
    db.commit()
    return 'deleted.'


def get(blog_id,  db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} is not available.')
    return blog


def update(blog_id, request: schemas.BlogRequest, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {blog_id} is not available.')
    blog.update(request.dict())
    db.commit()
    return 'updated.'
