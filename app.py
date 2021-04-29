from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'Welcome To barcelona FC'}

@app.get('/barcelona')
def index():
    return {'data': 'Messi, Fati, Griezman, Lenglet, Umtiti, Alba'}

@app.get('/barcelona/messi')
def index():
    return {'data': 'Name:Lionel Messi, Age:33,Nationality:Argentina'}

@app.get('/barcelona/alba')
def index():
    return {'data': 'Name:Jordi Alba, Age:30,Nationality:Spain'}

@app.get('/barcelona/pique')
def index():
    return {'data': 'Name:Gerard Pique, Age:31,Nationality:Spain'}