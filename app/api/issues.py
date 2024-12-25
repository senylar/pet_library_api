from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.issues_service import IssueService
from app.db.session import get_db
from app.models.issue import IssueCreate, IssueResponse

router = APIRouter()

@router.post("/", response_model=IssueResponse)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    """Создать выдачу книги читателю"""
    try:
        return IssueService.create_issue(db, issue)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id}", response_model=IssueResponse)
def get_issue(id: int, db: Session = Depends(get_db)):
    """Получить информацию о выдаче"""
    try:
        return IssueService.get_issue(db, id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}")
def close_issue(id: int, db: Session = Depends(get_db)):
    """Закрыть выдачу (вернуть книгу)"""
    try:
        return IssueService.close_issue(db, id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/")
def list_issues(db: Session = Depends(get_db)):
    """Получить список всех выдач"""
    try:
        return IssueService.get_all_issues(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
