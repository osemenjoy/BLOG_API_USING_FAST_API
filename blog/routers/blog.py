from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import models, schemas, database
from ..settings import get_db
from typing import List
from ..schemas import (
    ListBlog,
    BlogValidation
)
from sqlalchemy.orm import Session
from ..models import Blog, User


router = APIRouter()

@router.get('/blog', response_model=List[ListBlog], tags=["Blogs"]) # Add response model to redesign the way output is given
def get_all_blog(db:Session = Depends(get_db)):
    all_blogs = db.query(models.Blog).all()

    return all_blogs


@router.post('/create', status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create_blog(request: BlogValidation, db: Session = Depends(get_db)):
    title = request.title
    body = request.body
    new_blog = models.Blog(title=title, body=body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)    
    return {
        "message": "Blog created successfully",
        "blog": new_blog,
        "status_code": 201
    }


@router.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=["Blogs"], response_model=schemas.ListBlog)
def get_blog_by_id(id, response: Response, db: Session = Depends(get_db)):
    single_blog = db.query(Blog).filter(Blog.id == id).first()
    # single_blog

    if not single_blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Blog not found")
        # response.status_code = status.HTTP_404_NOT_FOUND

    return single_blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
def delete_blog(id, response: Response, db: Session = Depends(get_db)):
    single_blog = db.query(Blog).filter(Blog.id == id)

    if not single_blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Blog not found")
        # response.status_code = status.HTTP_404_NOT_FOUND

    single_blog.delete(synchronize_session=False)
    db.commit() # Always commit after delete or update or commit operations

    return {
        "message": "Blog deleted successfully"
    }


@router.put('/blog/{id}', status_code=status.HTTP_200_OK, tags=["Blogs"])
def update_blog(id, request: schemas.BlogValidation, response: Response, db: Session = Depends(get_db)):
    single_blog = db.query(Blog).filter(Blog.id == id)

    if not single_blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    single_blog.update(request.dict())
    db.commit() # Always commit after delete or update or commit operations

    return {
        "message": "Blog updated successfully"
    }

