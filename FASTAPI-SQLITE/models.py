from sqlalchemy import Column, Integer, String
from database import Base


class Books(Base): # this Books class inherit from Base in database.py file
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)
    

