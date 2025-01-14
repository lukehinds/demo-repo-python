from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import widget as widget_crud
from app.schemas.widget import Widget, WidgetCreate, WidgetUpdate
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Widget])
def read_widgets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    widgets = widget_crud.get_widgets(db, skip=skip, limit=limit)
    return widgets

@router.post("/", response_model=Widget)
def create_widget(widget: WidgetCreate, db: Session = Depends(get_db)):
    return widget_crud.create_widget(db, widget)

@router.get("/{widget_id}", response_model=Widget)
def read_widget(widget_id: int, db: Session = Depends(get_db)):
    widget = widget_crud.get_widget(db, widget_id)
    if widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")
    return widget

@router.put("/{widget_id}", response_model=Widget)
def update_widget(widget_id: int, widget: WidgetUpdate, db: Session = Depends(get_db)):
    updated_widget = widget_crud.update_widget(db, widget_id, widget)
    if updated_widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")
    return updated_widget

@router.delete("/{widget_id}", response_model=Widget)
def delete_widget(widget_id: int, db: Session = Depends(get_db)):
    widget = widget_crud.delete_widget(db, widget_id)
    if widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")
    return widget