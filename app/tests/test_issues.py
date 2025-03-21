import pytest
from fastapi.testclient import TestClient
from app.main import app  # Assuming your FastAPI app is in app/main.py
from app.db.session import get_db
from app.db.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_reader(test_db):
    response = client.post("/readers/", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_reader(test_db):
    # Create a reader first
    client.post("/readers/", json={"name": "John Doe"})
    response = client.get("/readers/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_list_readers(test_db):
    response = client.get("/readers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_reader(test_db):
    response = client.delete("/readers/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Читатель с ID 1 удален"