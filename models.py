from pydantic import BaseModel, Field, ValidationError, validator
from datetime import datetime

class Book(BaseModel):
    id: int
    title: str = Field(..., title='Name of book' ,min_length=1, max_length=100)
    author: str = Field(..., title='Name of author', min_length=1, max_length=50)
    year: int = Field(..., ge=1450, le=datetime.now().year)


