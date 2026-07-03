#LECTURE 2
#DYNAMIC ROUTE
from fastapi import FastAPI
app = FastAPI()

#USER ROUTE
@app.get("/users")
def get_user(user_id:int):
    return {
        "user_id" : user_id
    }