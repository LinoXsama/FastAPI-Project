from fastapi import FastAPI
from fastapi.params import Body

from pydantic import BaseModel

from typing import Optional

from random import randrange

app = FastAPI()

my_posts = [
   {
      "title": "London", "content": "Beautiful city !", "id": 1
   }, 
   {
      "title": "London", "content": "Beautiful city !", "id": 5
   }
]

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
   # print(post_data)
   post_dict = post_data.dict()
   # print(post_dict)
   post_dict['id'] = randrange(0, 1000000)
   # print(post_dict)
   my_posts.append(post_dict)
   return {"data": post_dict}