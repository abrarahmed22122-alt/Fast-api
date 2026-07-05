#LECTURE 8
#RESPONSE MODEL, DATA VALIDATION, HIGH SENSITIVE DATA

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class userdata(BaseModel):
    name : str
    roll_no : int

class Userresponse(BaseModel):
    name : str
    roll_no : int
    password : str

@app.get("/get_data", response_model=userdata)
def get_data():
    return {
        "name" : "abrar",
        "roll_no" : 1234,
        "last_name" : "ahmed",
        "password" : 12134

    }
