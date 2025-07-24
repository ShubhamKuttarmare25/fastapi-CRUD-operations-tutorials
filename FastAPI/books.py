from fastapi import FastAPI, HTTPException, Depends #HHTPException is used to define http specific error 
from pydantic import BaseModel, Field #used for data validation and putting constraints on data
from uuid import UUID
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session #imported Session from sqlalchemy getting errors

app = FastAPI()


models.Base.metadata.create_all(bind = engine) # this will create the new table if the table is not created 



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




#defined the Book
class Book(BaseModel):
    title: str =Field(min_length = 1)
    author: str = Field(min_length =1 , max_length = 100)
    description: str = Field(min_length =1 , max_length = 200)
    rating : int = Field(gt = -1 , lt = 101)



# this will be cleared everytime we reload this application as we are not using the database
BOOKS = [] # empty list for storing the Book 




@app.get("/") #here name is parameter 
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Books).all()


@app.post("/")
def create_book(book: Book, db: Session = Depends(get_db)):
    book_model = models.Books() 
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book







@app.put("/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)): # here book_id is path parameter and book is function parameter
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    #if this book_model is None return the httpsexception

    if book_model is None:
        raise HTTPException(
            status_code = 404,
            details = f"The book with book ID {book_id} does not exist"
        )
    

    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating  = book.rating

    db.add(book_model)
    db.commit()

    return book








@app.delete('/{book_id}')
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()


    if book_model is None:
        raise HTTPException(
            status_code = 404,
            details= f"The book with book ID {book_id} does not exist"
        )
    

    db.query(models.Books).filter(models.Books.id == book_id).delete()

    db.commit()
    