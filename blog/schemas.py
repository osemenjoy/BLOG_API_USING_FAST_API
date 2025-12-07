from pydantic import BaseModel
from typing import List

class BlogValidation(BaseModel):
    title: str
    body: str

class User(BaseModel):
    username: str
    email: str
    password: str

class RetrieveUser(BaseModel):
    username: str
    email: str
    blogs: List[BlogValidation]
    
    class Config():
        from_attributes = True

class ListBlog(BlogValidation):
    title: str
    body: str
    creator: RetrieveUser

    # Make ORM true to use response model
    #! Read more on this
    class Config():
        from_attributes = True # orm mode has been changed to from_attributes 


