from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..repository import users


router = APIRouter(
    prefix='/users',
    tags=['users']
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return users.create(user, db)


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(user_id, db: Session = Depends(get_db)):
    return users.get(user_id, db)
