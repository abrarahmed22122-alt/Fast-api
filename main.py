# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def home():
#     return {
#         "Message":"pytest"
#     }

# @app.get("/add")
# def add(a:int,b:int):
#     return {
#         "result":a+b
#     }

# from fastapi import FastAPI
# import requests

# app = FastAPI()

# @app.get("/posts")
# def get_posts():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     response = requests.get(url)
#     return response.json()

# #Get Single Post
# @app.get("/posts/{post_id}")
# def get_post(post_id:int):
#     url = "https://jsonplaceholder.typicode.com/posts"
#     response = requests.get(url)
#     return response.json()

# from fastapi import FastAPI
# import requests
# from bs4 import BeautifulSoup

# app = FastAPI()
# @app.get("/News")
# def get_news():
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN%3Aen"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text,"html.parser")

#     title = []

#     for items in soup.find_all("a",class_ = "WwrzSb"):
#         title.append(items.text)

#     return{
#         "News":title
#     }


from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

#limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

#Error Handle
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request:Request,exc:RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content = {
            "detail" : "Too many requests"
        }
    )

#Rate Limiter API
@app.get("/data")
@limiter.limit("5/minute")
def get_data(request:Request):
    return {
        "Message":"Success"
    }