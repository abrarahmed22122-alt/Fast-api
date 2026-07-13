#LECTURE 11 
# DEPENDS(), REUSABLE LOGIC, AUTH EXAMPLE INTRO

from fastapi import FastAPI, Depends, Header, HTTPException
app = FastAPI()

def reduce_repetition():
    name = "abrar"
    return {
        "Message" : name
    }

@app.get("/reusablelogic")
def return_same_logic(data:str = Depends(reduce_repetition)):
    return  data

def verify_token(token:str=Header(None)):
    if token != "mytoken":
        raise HTTPException(
            status_code = 404,
            detail = "Unauthorized"
        )
    return {
        "user" : "Authorized user"
    }

@app.get("/authorized_user")
def authorize_user(User:dict = Depends(verify_token)):
    return{
        "Message" : "Secure Data Accessed",
        "User" : User
    }
