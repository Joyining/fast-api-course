from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import users


router = APIRouter(
    prefix='/users',
    tags=['users'],
    dependencies=[Depends(oauth2.get_current_user)]
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserRequest, db: Session = Depends(get_db)):
    return users.create(user, db)


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
def get_user(user_id, db: Session = Depends(get_db)):
    return users.get(user_id, db)
