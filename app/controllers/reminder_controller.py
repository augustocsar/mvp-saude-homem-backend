from fastapi import HTTPException, status
from typing import List
from app.schemas.reminder import ReminderCreate, ReminderUpdate, ReminderInDB
from app.services import reminder_service

async def get_all_reminders() -> List[ReminderInDB]:
    return await reminder_service.get_reminders()

async def get_reminder_by_id(reminder_id: int) -> ReminderInDB:
    reminder = await reminder_service.get_reminder(reminder_id)
    if not reminder:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reminder not found")
    return reminder

async def create_new_reminder(reminder: ReminderCreate) -> ReminderInDB:
    return await reminder_service.create_reminder(reminder)

async def update_existing_reminder(reminder_id: int, reminder_update: ReminderUpdate) -> ReminderInDB:
    updated = await reminder_service.update_reminder(reminder_id, reminder_update)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reminder not found")
    return updated

async def delete_reminder_by_id(reminder_id: int) -> None:
    deleted = await reminder_service.delete_reminder(reminder_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reminder not found")
