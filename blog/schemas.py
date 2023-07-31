from typing import Optional, List
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class BaseBlog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

    class Config():
        orm_mode = True


class BaseUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class BlogRequest(BaseBlog):
    pass


class UserRequest(BaseModel):
    name: str
    email: str
    password: str


class BlogResponse(BaseModel):
    title: str
    body: str
    creator: BaseUser

    class Config():
        orm_mode = True


class UserResponse(BaseModel):
    name: str
    email: str
    blogs: List[BaseBlog]

    class Config():
        orm_mode = True
