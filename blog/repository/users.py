from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..hashing import Hash


def create(user, db: Session):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=Hash.bcrypt(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(user_id, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} is not available.')
    return user
