from sqlalchemy.orm import Session
from app.models.widget import Widget
from app.schemas.widget import WidgetCreate, WidgetUpdate

def get_widget(db: Session, widget_id: int):
    return db.query(Widget).filter(Widget.id == widget_id).first()

def get_widgets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Widget).offset(skip).limit(limit).all()

def create_widget(db: Session, widget: WidgetCreate):
    db_widget = Widget(**widget.model_dump())
    db.add(db_widget)
    db.commit()
    db.refresh(db_widget)
    return db_widget

def update_widget(db: Session, widget_id: int, widget: WidgetUpdate):
    db_widget = get_widget(db, widget_id)
    if db_widget:
        for key, value in widget.model_dump(exclude_unset=True).items():
            setattr(db_widget, key, value)
        db.commit()
        db.refresh(db_widget)
    return db_widget

def delete_widget(db: Session, widget_id: int):
    db_widget = get_widget(db, widget_id)
    if db_widget:
        db.delete(db_widget)
        db.commit()
    return db_widget