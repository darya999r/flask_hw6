import datetime
from fastapi import FastAPI, HTTPException
# import database as db
# import models
from typing import List
from random import randint


app = FastAPI()


@app.get("/")
def root():
    return {"Message": "Hello, root!"}