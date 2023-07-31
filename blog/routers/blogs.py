from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from typing import List
from ..repository import blogs

router = APIRouter(
    prefix='/blogs',
    tags=['blogs'],
    dependencies=[Depends(oauth2.get_current_user)]
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.BlogRequest, db: Session = Depends(get_db)):
    return blogs.create(blog, db)


# https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.delete
@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    return blogs.delete(blog_id, db)


@router.get('/', response_model=List[schemas.BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    return blogs.get_all(db)


@router.get('/{blog_id}', status_code=status.HTTP_200_OK, response_model=schemas.BlogResponse)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return blogs.get(blog_id, db)


# https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.update
@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id, request: schemas.BlogRequest, db: Session = Depends(get_db)):
    return blogs.update(blog_id, request, db)
