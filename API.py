from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    age: int
    height: int
    email: str

app = FastAPI()

@app.post("/users/")
async def create_user(user: User):
    # pending connect with database to store the user data
    print(user)
    return user





