# data to object (object definition)

from pydantic import BaseModel
import datetime

class DailyMetrics(BaseModel, arbitrary_types_allowed=True):
    user_id: int
    date: datetime
    mood: str
    energy: str
    appetite: str
    cravings: str
    sleep_quality: str
    sleep_time: int
    workout_time: int
    workout_type: str
