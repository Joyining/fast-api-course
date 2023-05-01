from typing import Optional, List
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class BaseBlog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


class Blog(BaseBlog):

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True
