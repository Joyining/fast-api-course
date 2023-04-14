from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import uvicorn

# create instance
app = FastAPI()


@app.get('/')
def index():
    return 'Hey'


@app.get('/about')
def about():
    return {'data': {'about': 'This is us.'}}


@app.get('/blogs')
def get_blogs(limit=50, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': {'blogs': f'Showing {limit} published blogs.'}}
    else:
        return {'data': {'blogs': f'Showing {limit} blogs.'}}


@app.get('/blogs/unpublished')
def get_unpublished_blogs():
    return {'data': {'blogs': 'All unpublished blogs.'}}


@app.get('/blogs/{blog_id}')
def get_blog(blog_id: int):
    return {'data': blog_id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
# you can name it whatever you want.
def create_blog(blog: Blog):
    return {'data': f'A blog was created with the title {blog.title}.'}


# change the port when you run python3 main.py
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=9000)
