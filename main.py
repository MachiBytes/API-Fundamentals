from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import Book, BookInput

app = FastAPI()

@app.get("/")
def read_root():
    response = {"message": "API is running!"}
    return JSONResponse(content=response, status_code=202)

@app.get("/books")
def get_books():
    books = [{"id": book.id, "title": book.title, "author": book.author} for book in Book.select()]
    response = {
        "message": "Successfully retrieved all books.",
        "books": books
    }
    return JSONResponse(content=response, status_code=200)

@app.get("/books/search")
def search_books(author: str):
    books = [{"title": book.title, "author": book.author} for book in Book.select().where(Book.author.contains(author))]
    return {"books": books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = Book.get_or_none(Book.id == book_id)
    if not book:
        return {"error": "Book not found"}, 404
    return {"title": book.title, "author": book.author}

@app.post("/books")
def create_book(book: BookInput):
    new_book = Book.create(title=book.title, author=book.author)
    return {"id": new_book.id, "title": new_book.title}

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    existing_book = Book.get_or_none(Book.id == book_id)
    if not existing_book:
        return {"error": "Book not found"}, 404
    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.save()
    return {"message": "Book updated", "book": existing_book}

