#LECTURE 10
#HTTP EXCEPTION, CUSTOM EXCEPTIONS, GLOBAL ERROR HANDLING

from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse
app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.get("/data_fetch/{name}")
def get_user(name:str):
    if name != "abrar":
        raise UserNotFoundException(name)
    return {
        "name" : name
    }

@app.exception_handler(UserNotFoundException)
def User_Not_Found_Handler(request:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code = 404,
        content = {
            "status" : "error",
            "message" : f"user{exc.name} not found"
        }
    )