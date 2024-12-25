from fastapi import APIRouter, HTTPException
from app.models import Book
from app.database import add_book, get_books, get_all_books, update_book, delete_book

router = APIRouter()

@router.get("/books")
async def read_books():
    books = await get_books()
    return books

@router.get("/books/all")
async def read_all_books():
    books = await get_all_books()
    return books

@router.post("/books/addBook")
async def add_book_h(book: Book):
    result = await add_book(book)
    return {'message': 'Book added successfully', 'data': book.json()}

@router.put("/books/updateBook/{book_id}")
async def update_books(book_id: int, update_data: dict):
    result = await update_book(book_id, update_data)
    if result is None:
        raise HTTPException(status_code=400, detail="Book not found or no fields to update")
    return {'message': 'Book updated successfully', 'data': result}

@router.delete("/books/deleteBook/{book_id}")
async def delete_books(book_id: int):
    result = await delete_book(book_id)
    if result is None:
        raise HTTPException(status_code=400, detail="Book not found")
    return {'message': 'Book deleted successfully', 'data': result}