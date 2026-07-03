from fastapi import FastAPI
app = FastAPI()

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