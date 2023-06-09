from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash

router = APIRouter(
    tags=['authentication']
)
get_db = database.get_db


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail='Invalid Credential')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            detail='Incorrect Password')
    return user
