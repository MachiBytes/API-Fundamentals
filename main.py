from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import Book

app = FastAPI()

@app.get("/")
def read_root():
    response = {"message": "API is running!"}
    return JSONResponse(content=response, status_code=202)

@app.get("/books")
def get_books():
    books = [{"title": book.title, "author": book.author} for book in Book.select()]
    response = {
        "message": "Successfully retrieved all books.",
        "books": books
    }
    return JSONResponse(content=response, status_code=200)
