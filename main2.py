#LECTURE 3
#QUERY PARAMETER

from fastapi import FastAPI
app = FastAPI()
@app.get("/users")
def get_users(name:str=None):
    return {"Name":name}

@app.get("/Products")
def get_users(limit:int=10):
    return{
        "limit":limit
    }