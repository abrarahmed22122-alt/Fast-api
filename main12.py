#LECTURE 13
#SQLITE, SETUP DB, CONNECT FASTAPI WITH DB, SQLITE VS SQLALCHEMY

import sqlite3
from fastapi import FastAPI
app = FastAPI()

conn1 = sqlite3.connect("test1.db", check_same_thread = False)
cursor = conn1.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS todoS(
               id INTEGER PRIMARY KEY,
               title TEXT,
               Completed TEXT)
""")
conn1.commit()

@app.get("/home")
def home():
    return {
        "Message" : "sqlite3 connect with fastapi"
    }