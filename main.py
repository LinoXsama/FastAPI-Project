from fastapi import FastAPI, Response, status
from fastapi.params import Body

from pydantic import BaseModel

from typing import Optional

from random import randrange

app = FastAPI()


# Définition du modèle auquel doit répondre un post !
class Post(BaseModel):
   title: str
   content: str
   published: bool = True
   rating: Optional[int] = None

my_posts = [
   {
      "title": "London",
      "content": "Beautiful city !",
      "id": 1
   }, 
   {
      "title": "Moscow",
      "content": "Cloudy city !",
      "id": 5
   }
]

def find_post(id):
   for p in my_posts:
      if p["id"] == id:
         return p

# Route racine / !
@app.get("/")
async def root():
   return {"message": "Welcome to my API !"}

# Route /posts permettant d'obtenir tous les posts !
@app.get("/posts")
def get_posts():
   return {"data": my_posts}

# Route permettant d'obtenir le post le plus récent !
@app.get("/posts/latest")
def get_latest_post():
   post = my_posts[len(my_posts) - 1]
   return {"detail": post}

# Route /posts/{id} permettant d'obtenir un post en fonction de son id !
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
   post = find_post(int(id))
   if not post:
      response.status_code = status.HTTP_404_NOT_FOUND 
   return {"post_detail": post}

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