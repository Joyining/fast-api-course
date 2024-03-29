from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..hashing import Hash

router = APIRouter(
    tags=['authentication']
)
get_db = database.get_db


@router.post('/login')
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail='Invalid Credential')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            detail='Incorrect Password')

    access_token = token.create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': "bearer"}
