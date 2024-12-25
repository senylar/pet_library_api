

from fastapi import FastAPI, HTTPException
from app.routres import router
app = FastAPI(
    title="Books API",
    description="Simple API for books",
    version="0.1"
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(router)