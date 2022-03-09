import string
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Data(BaseModel):
    name:Optional[str] = None
    email:Optional[str] = None

app = FastAPI()

@app.get("/")
def hello():
    return { "message":"Hi there!" }

@app.post("/get-data")
async def get_info(data:Data):
    print(data)
    return { "message":"Ok" }