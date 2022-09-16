from fastapi import FastAPI
from src.models import User_model

app = FastAPI()

@app.get('/')
def root():
    return {"hello": "world"}

@app.post('/')
def root(deen: User_model.User):
    return deen
