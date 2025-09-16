from typing import List, Optional
from app.schemas.reminder import ReminderCreate, ReminderUpdate,  ReminderInDB
from datetime import datetime

# Lista que vai armazenar os lembretes em memória
reminders_db: List[ReminderInDB] = []
current_id = 1

async def get_reminders() -> List[ReminderInDB]:
    return reminders_db

async def get_reminder(reminder_id: int) -> Optional[ReminderInDB]:
    for reminder in reminders_db:
        if reminder.id == reminder_id:
            return reminder
    return None

async def create_reminder(reminder: ReminderCreate) -> ReminderInDB:
    global current_id
    new_reminder = ReminderInDB(id=current_id, **reminder.dict())
    reminders_db.append(new_reminder)
    current_id += 1
    return new_reminder

async def update_reminder(reminder_id: int, reminder_update: ReminderUpdate) -> Optional[ReminderInDB]:
    for index, reminder in enumerate(reminders_db):
        if reminder.id == reminder_id:
            updated_data = reminder.dict()
            update_fields = reminder_update.dict(exclude_unset=True)
            updated_data.update(update_fields)
            updated_reminder = ReminderInDB(**updated_data)
            reminders_db[index] = updated_reminder
            return updated_reminder
    return None

async def delete_reminder(reminder_id: int) -> bool:
    for index, reminder in enumerate(reminders_db):
        if reminder.id == reminder_id:
            reminders_db.pop(index)
            return True
    return False
