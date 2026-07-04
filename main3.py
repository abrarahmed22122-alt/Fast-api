#LECTURE 4
#REQUEST BODY,JSON INPUT HANDLING, POST REQUEST,INTRO TO PYDANTIC

from fastapi import FastAPI
app = FastAPI()

@app.post("/create_user")
def create_user(name:str,age:int):
    return {
        "Name" : name,
        "Age" : age
    }
