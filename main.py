from fastapi import FastAPI
from fastapi.params import Body

from pydantic import BaseModel

from typing import Optional

app = FastAPI()

my_posts = [{"title": "London", "content": "Beautiful city !", "id": 1}, {"title": "London", "content": "Beautiful city !", "id": 1}]

class Post(BaseModel):
   title: str
   content: str
   published: bool = True
   rating: Optional[int] = None

@app.get("/")
async def root():
   return {"message": "Welcome to my API !"}

@app.get("/posts")
def get_posts():
   return {"data": my_posts}

@app.post("/posts")
def create_post(post_data: Post):
	print(post_data)
	print(post_data.dict())
	return {"data": post_data}