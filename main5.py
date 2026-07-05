#LECTURE 6 
#CRUD OPERATION 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#create data by using post api

todos = []
class Todo(BaseModel):
    email : str
    phone_n :int
    id : int 
    title : str
    completed : bool

@app.post("/create_data")
def create_data(todo:Todo):
    todos.append(todo)
    return {
        "Message":"TODO ADDED","data":todo
    }

@app.get("/read_data")
def read_data():
    return todos

@app.get("/read_data/{todo_id}")
def get_data(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {
        "error" : "Todo not found" 
    }

@app.put("/update_data/{todo_id}")
def update_todo(todo_id:int,update_data:Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_data
            return {
                "Message":"data updated",
                "Data" : update_data
            }
        
@app.delete("/delete_data/{todo_id}")
def delete_data(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return{
                "Message":"Data Deleted",
                "data" : todos
            }
    return {
        "error" : "Todo not found in todos"
    }