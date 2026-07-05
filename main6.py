#lecture 7
# PATH + QUERY + BODY COMBO

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []

class data(BaseModel):
    name : str
    roll_no : int
    title : str

@app.post("/create_data/{data_is}")
def create_data(user:data):
    users.append(user)
    return {
        "Message": " data created Succesfully",
        "data" : user
    }

@app.get("/get_data")
def get_data():
    return{
        "data" : users
    }

@app.put("/update_data/{data_is}")
def updated_data(data_is:int,update_data:data,notify:bool=False):
    if data_is < len(users):
        users[data_is] = update_data
        return {
            "Message":"User Updated",
            "notify" : notify,
            "data" : users
        }
    return {
        "error" : "todo not found"
    }