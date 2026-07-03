#lecture 1 -- Basic Route of fastapi

from fastapi import FastAPI
app = FastAPI()
#home route
@app.get("/")
def home():
    return {
        "Message":"WELCOME TO FASTAPI"
    }

#About route
@app.get("/about")
def about():
    return {
        "Message":"This is about page"
    }