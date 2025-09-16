from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReminderBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime

class ReminderCreate(ReminderBase):
    pass

class ReminderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None

class ReminderInDB(ReminderBase):
    id: int

    class Config:
        orm_mode = True
