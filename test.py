from pydantic import BaseModel, Field

def lower(s):
    return s.upper()

class User(BaseModel):
    id: int
    name: str
    age: int = Field(..., gt=0)
    test : str = Field(default_factory=lambda: lower('default'))


user = User(id=0, name='John Doe', age=30, test='hui')
print(user.dict())
print(user.json())
print(user.construct())
print(user.model_dump())

