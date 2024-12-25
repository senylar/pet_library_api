from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.books_service import BookService
from app.db.session import get_db
from app.models.book import BookCreate, BookResponse

router = APIRouter()

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Создать книгу"""
    try:
        return BookService.create_book(db, book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=BookResponse)
def get_book(id: int, db: Session = Depends(get_db)):
    """Получить информацию о книге"""
    try:
        book = BookService.get_book(db, id)
        if not book:
            raise ValueError("Книга не найдена")
        return book
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    """Удалить книгу"""
    try:
        return BookService.delete_book(db, id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/")
def list_books(db: Session = Depends(get_db)):
    """Получить список всех книг"""
    try:
        return BookService.get_all_books(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
