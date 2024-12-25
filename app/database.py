import asyncio

import aiosqlite as sql

from app.models import Book
from config import db_path
print(db_path)

async def add_book(book):
    try:
        async with sql.connect(db_path) as conn:
            query = f"INSERT INTO Books (title, author, year) VALUES ('{book.title}', '{book.author}', {book.year})"
            await conn.execute(query)
            await conn.commit()
            return query
    except Exception as e:
        raise e

async def get_books():
    async with sql.connect(db_path) as conn:
        query = "SELECT * FROM Books"
        cursor = await conn.execute(query)
        books = await cursor.fetchall()
        return books

async def get_all_books():
    async with sql.connect(db_path) as conn:
        query = "SELECT * FROM Books"
        cursor = await conn.execute(query)
        books = await cursor.fetchall()
        return books

async def update_book(book_id, update_data: dict):
    # Динамически собираем список полей для обновления
    fields = []
    params = []

    if "title" in update_data:
        fields.append("title = ?")
        params.append(update_data["title"])

    if "author" in update_data:
        fields.append("author = ?")
        params.append(update_data["author"])

    if "year" in update_data:
        fields.append("year = ?")
        params.append(update_data["year"])

    # Если ничего не обновлять, можно либо вернуть None, либо выбросить исключение
    if not fields:
        return None

    # Собираем финальный SQL-запрос
    query = "UPDATE Books SET " + ", ".join(fields) + " WHERE id = ?"
    params.append(book_id)

    async with sql.connect(db_path) as conn:
        await conn.execute(query, params)
        await conn.commit()

    return query

async def delete_book(book_id):
    query = f"DELETE FROM Books WHERE id = {book_id}"
    async with sql.connect(db_path) as conn:
        await conn.execute(query)
        await conn.commit()
    return query