# API entrance

from fastapi import FastAPI
from dto.user import User
from services.users import insertUser
from dto.dailymetric import DailyMetrics
from services.dailymetrics import insertDailyMetric

app = FastAPI()

@app.post("/users/")
async def CreateUser(user: User):
    insertUser(user)
    return user

@app.post("/dailymetrics/")
async def CreateDailyMetrics(dailymetric: DailyMetrics):
    insertDailyMetric(dailymetric)
    return dailymetric


