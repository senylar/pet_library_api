from models import Book

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id):

    try:
        id = int(item_id)
        return {"item_id": item_id}
    except ValueError:
        return 500, "Item not found"

@app.post("/books/addBook")
async def add_book(book : Book):

    return {'message':'Book added successfully',
        'data':book.json()}