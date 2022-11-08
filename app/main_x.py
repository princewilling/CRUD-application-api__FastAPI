from pyexpat import model
from typing import Optional
from unittest.main import MODULE_EXAMPLES
from fastapi import Body, FastAPI, Depends, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .db import models
from .db.database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None
    
while True:
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(host='localhost', 
                                database='fastapi crud system', user='princewillingoo', 
                                password="1234", 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Succesfully Connected To DB")
        break
    except Exception as error:
        print("Failed To Connect DB")
        print(error)
        time.sleep(3)

    
my_posts = [{"title":"machine learning", "content":"machine can read and write", "id":1},
           {"title":"data engineering", "content":"building relaible data system", "id":2},
           {"title":"software engineering", "content":"building relaible software products", "id":3}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    
    posts = db.query(models.Post).all()
    print(posts)
    return {"data": posts}

@app.get("/")
async def root():
    return{"message": "welcome to my api"}

@app.get("/posts")
async def get_post(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    #print(posts)
    posts = db.query(models.Post).all()
    
    return{"data": posts }

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db)):
    
    
    new_post = models.Post(
        **post.dict()
    )
    # post = models.Post(
    #     title=post.title, content=post.content, published=post.published
    # )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    # cursor.execute(
    #     """
    #     INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING * 
    #     """, 
    #     (post.title, post.content, post.published)
    # )
    # post = cursor.fetchone()
    # conn.commit()
    
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0, 1000000)
    # # convert pydantic to dictionary
    # my_posts.append(post_dict)
    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response, db: Session = Depends(get_db)):
    # cursor.execute(
    #     """
    #     SELECT * from posts WHERE id = %s
    #     """,
    #     (str(id))
    # )
    # post = cursor.fetchone()
    
    # post = find_post(id)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:{id} was not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return {"post_detail":post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # deleting post
    # cursor.execute(
    #     """
    #     DELETE FROM posts WHERE id = %s RETURNING *
    #     """,
    #     (str(id),)
    # )
    # deleted_post = cursor.fetchone()
    # conn.commit()
    
    #index = find_index_post(id)
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    # my_posts.pop(index)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, updated_post:Post, db: Session = Depends(get_db)):
    # cursor.execute(
    #     """
    #     UPDATE posts SET title =%s, content=%s, published=%s WHERE id =%s RETURNING *
    #     """,
    #     (post.title, post.content, post.published, str(id))
    # )
    # #index = find_index_post(id)
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
        
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    # post_dict = post.dict()
    # post_dict["id"]= id
    # my_posts[index] = post_dict
        
    return{"data": post_query.first()}