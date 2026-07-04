#LECTURE 5
# DATA VALIDATION, CREATE SCHEMAS, NESTED MODEL

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    age : int
    subject : str
    college : str

@app.post("/create_user")
def create_user(user:User):
    return {
        "Message":"Data Validation",
        "Data" : user
    }
 
class User1(BaseModel):
    first_name:str
    last_name: str
    dob : int

class User2(BaseModel):
    time : int
    data : User1

@app.post("/create_users")
def data_user(data_appear:User2):
    return{
        "data": data_appear
    }