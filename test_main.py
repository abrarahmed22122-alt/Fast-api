# from fastapi.testclient import TestClient
# from main import app
# client = TestClient(app)

# #Test Home Api
# def test_home():
#     response = client.get("/")

#     #Status codepip install pytest
#     assert response.status_code == 200

#     #Response data check
#     assert response.json() == {
#         "Message":"pytest"
#     }

# #Test App Api
# def Test_Add():
#     response = client.get("/add?a=5&b=2")
#     assert response.status_code == 200
#     assert response.json() == {"result:8"}

from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

#Get Single Post
@app.get("/posts/{post_id}")
def get_post(post_id:int):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()
