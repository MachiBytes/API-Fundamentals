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

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = Book.get_or_none(Book.id == book_id)
    if not book:
        return {"error": "Book not found"}, 404
    return {"title": book.title, "author": book.author}

@app.get("/books/search")
def search_books(author: str):
    books = [{"title": book.title} for book in Book.select().where(Book.author == author)]
    return {"books": books}
