from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

""" Child
1. 在 Child 使用 ForeignKey 去 reference Parent (users 表中的欄位 id) 
2. 在 Parent 使用 relationship() 去 reference a list of Child 
Note: 使用 relationship() 的 attributes 是不出現在 table 裡的
3. 因為這個關係是雙向的，所以必須用 back_populates 表明這個雙向關係 """


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))  # 1

    creator = relationship('User', back_populates='blogs')  # 3


""" Parent (一個 user 會有多個 blog) """


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates='creator')  # 2
