from fastapi import FastAPI
from fastapi.params import Body

from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
   title: str
   content: str

@app.get("/")
async def root():
   return {"message": "Welcome to my API !"}

@app.get("/posts")
def get_posts():
   return {"data": "This is your posts"}

@app.post("/createpost")
def create_post(post_data: Post):
	print(post_data)
	print(post_data.title)
	print(post_data.content)
	return {"data": "new post"}