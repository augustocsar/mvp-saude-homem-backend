from fastapi import APIRouter
from typing import List
from app.controllers import reminder_controller
from app.schemas.reminder import ReminderCreate, ReminderUpdate, ReminderInDB

router = APIRouter(prefix="/reminders", tags=["reminders"])

@router.get("/", response_model=List[ReminderInDB])
async def list_reminders():
    return await reminder_controller.get_all_reminders()

@router.get("/{reminder_id}", response_model=ReminderInDB)
async def get_reminder(reminder_id: int):
    return await reminder_controller.get_reminder_by_id(reminder_id)

@router.post("/", response_model=ReminderInDB, status_code=201)
async def create_reminder(reminder: ReminderCreate):
    return await reminder_controller.create_new_reminder(reminder)

@router.put("/{reminder_id}", response_model=ReminderInDB)
async def update_reminder(reminder_id: int, reminder_update: ReminderUpdate):
    return await reminder_controller.update_existing_reminder(reminder_id, reminder_update)

@router.delete("/{reminder_id}", status_code=204)
async def delete_reminder(reminder_id: int):
    await reminder_controller.delete_reminder_by_id(reminder_id)
    return None
