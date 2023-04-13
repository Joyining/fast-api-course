from fastapi import FastAPI

# create instance
app = FastAPI()


@app.get('/')
def index():
    return 'Hey'


@app.get('/about')
def about():
    return {'data': {'about': 'This is us.'}}
