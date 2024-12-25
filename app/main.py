from fastapi import FastAPI
from app.api import books, issues, readers

app = FastAPI(
    title="Library API",
    description="API для управления библиотекой",
    version="1.0.0"
)

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(readers.router, prefix="/readers", tags=["Readers"])
app.include_router(issues.router, prefix="/issues", tags=["Issues"])

