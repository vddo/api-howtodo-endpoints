from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import uvicorn

app = FastAPI()
   
users = [
    {"id": str(uuid.uuid4()), "username": "johndoe", "email": "john@mail.com"},
    {"id": str(uuid.uuid4()), "username": "pranav", "email": "pranav@mail.com"},
    {"id": str(uuid.uuid4()), "username": "emily", "email": "emily@mail.com"}
]

# Pydantic model
class User(BaseModel):
    username: str
    email: str

# Endpoints
@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: str):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"message": "User not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)    
