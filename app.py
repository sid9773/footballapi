from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')
def index(limit):
    return {'data': f'{limit} blogs are here'}

@app.get('/barcelona')
def index():
    return {'data': 'Messi, Fati, Griezman, Lenglet, Umtiti, Alba'}

@app.get('/barcelona/messi')
def index():
    return {'data': 'Name:Lionel Messi, Age:33,Nationality:Argentina'}

@app.get('/barcelona/alba')
def index():
    return {'data': 'Name:Jordi Alba, Age:30,Nationality:Spain'}

@app.get('/barcelona/{id}')
def index(id:int):
    return {'data': id}
    