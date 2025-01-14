from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WidgetBase(BaseModel):
    name: str
    description: Optional[str] = None

class WidgetCreate(WidgetBase):
    pass

class WidgetUpdate(WidgetBase):
    pass

class Widget(WidgetBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True