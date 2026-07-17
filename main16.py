#Lecture 17
#async/await
from fastapi import FastAPI
import time,asyncio
app = FastAPI()

@app.get("/sync")
def sync():
    time.sleep(3)
    return "Sync operation"



@app.get("/data")
async def task():
    time.sleep(3)
    return "Async Operation"


