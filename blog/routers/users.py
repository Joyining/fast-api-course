from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash

router = APIRouter()


@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['users'])
def create_user(user: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/users/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['users'])
def get_user(user_id, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} is not available.')
    return user
