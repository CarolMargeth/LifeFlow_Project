# API entrance

from fastapi import FastAPI
from dto.user import User
from psycopgPOST import insertUser
    
app = FastAPI()

@app.post("/users/")
async def CreateUser(user: User):
    insertUser(user)
    # print(user)
    return user




