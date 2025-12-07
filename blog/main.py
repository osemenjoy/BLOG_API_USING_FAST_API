from fastapi import FastAPI, Depends, status ,Response, HTTPException
from blog.schemas import BlogValidation, ListBlog
from blog import models, schemas
from blog.database import engine
from blog.settings import get_db
from sqlalchemy.orm import Session
from blog.models import Blog, User
from typing import List
from passlib.context import CryptContext
from .hashing import Hashing
from blog.routers import blog, user

# creaing the tables in the database, this creates all the tables in the database
models.Base.metadata.create_all(engine)
app = FastAPI()

    
app.include_router(blog.router)
app.include_router(user.router)