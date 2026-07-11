#LECTURE 9
#HTTP STATUS CODE, CUSTOM RESPONSE, ERROR HANDLING BASICS

from fastapi import FastAPI, status, HTTPException
app = FastAPI()

@app.post("/create_user",status_code=status.HTTP_302_FOUND)
def create_user():
    return{
        "Message":"Data Created"
    }

@app.get("/user_data")
def user_data():
    return {
        "status" : "Success",
        "Message" : "Data Created by the user",
        "data" : {
            "Name" : "abrar",
            "Age":21

        }
    }

@app.get("/data_user/{user_id}")
def data_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail = "User Not Found"
        )
    return {
        "id" : 1,
        "Name" : "Mohit"
    }
    
