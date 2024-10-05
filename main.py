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

# Définition du modèle auquel doit répondre un post !
class Post(BaseModel):
   title: str
   content: str
   published: bool = True
   rating: Optional[int] = None

# Route racine / !
@app.get("/")
async def root():
   return {"message": "Welcome to my API !"}

# Route /posts permettant d'obtenir tous les posts !
@app.get("/posts")
def get_posts():
   return {"data": my_posts}

# Route /posts/{id} permettant d'obtenir un post en fonction de son id !
@app.get("/posts/{id}")
def get_post(id):
   print(id)
   return {"post_detail": f"Here is post {id}"}

# Route /posts permettant de créer un post !
@app.post("/posts")
def create_post(post_data: Post):
   # print(post_data)
   post_dict = post_data.dict()
   # print(post_dict)
   post_dict['id'] = randrange(0, 1000000)
   # print(post_dict)
   my_posts.append(post_dict)
   return {"data": post_dict}