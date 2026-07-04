#LECTURE 4
#REQUEST BODY,JSON INPUT HANDLING, POST REQUEST,INTRO TO PYDANTIC

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name : str
    age : int
@app.post("/createuser")
def createuser(user:User):
    return{
    "Message":"user created",
    "data" : user
    }


@app.post("/create_user")
def create_user(name:str,age:int):
    return {
        "Name" : name,
        "Age" : age
    }



