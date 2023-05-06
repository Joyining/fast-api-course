from fastapi import FastAPI
from . import models
from .database import engine
from .routers import authentication, blogs, users

app = FastAPI()

""" 通過調用 Base.metadata.create_all(engine)
其中 engine 是之前使用 create_engine 建立的資料庫引擎
可以根據模型定義自動建立資料庫表格
這將根據 Base 下的所有繼承類別定義，生成相應的資料庫表結構 """
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)
