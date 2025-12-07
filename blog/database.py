"""
    Creating the database connection for sqlite to fastapi
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# defining the database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# creating engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# define the session local
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# creating base
Base = declarative_base()