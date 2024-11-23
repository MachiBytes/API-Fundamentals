from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from database import Book, BookInput

app = FastAPI()

API_KEY = "this_is_our_secret_key"

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(request.headers)
        auth_header = request.headers.get("authorization")
        
        # Check if the header exists and follows the "Bearer <token>" format
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(content={"error": "Missing or invalid Authentication header"}, status_code=401)
        
        # Extract the token
        token = auth_header.split(" ")[1]
        
        # Validate the token
        if token != API_KEY:
            return JSONResponse(content={"error": "Invalid API key"}, status_code=401)
        
        # Proceed to the next request handler
        return await call_next(request)

# Add the middleware to the app
app.add_middleware(AuthenticationMiddleware)

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
        return JSONResponse(content={"error": "Book not found"}, status_code=404)
    return {"title": book.title, "author": book.author}

@app.post("/books")
def create_book(book: BookInput):
    new_book = Book.create(title=book.title, author=book.author)
    return {"id": new_book.id, "title": new_book.title}

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    existing_book = Book.get_or_none(Book.id == book_id)
    if not existing_book:
        return JSONResponse(content={"error": "Book not found"}, status_code=404)
    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.save()
    return {"message": "Book updated", "book": existing_book}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = Book.get_or_none(Book.id == book_id)
    if not book:
        return JSONResponse(content={"error": "Book not found"}, status_code=404)
    book.delete_instance()
    return {"message": "Book deleted"}
