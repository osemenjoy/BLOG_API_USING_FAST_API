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
from ..hashing import Hashing


router = APIRouter()

@router.post('/user', status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username, email=request.email, password=Hashing.bcrypt(request.password))

    # create user
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "new user created successfully"
    }


# retrieve a single user
@router.get('/user/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.RetrieveUser, tags=["Users"])
def get_user(user_id, db: Session = Depends(get_db)):
    single_user = db.query(User).filter(User.id== user_id).first()

    if not single_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return single_user