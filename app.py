from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'Welcome To barcelona FC'}