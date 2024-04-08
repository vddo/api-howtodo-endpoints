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

@app.post("/users")
def create_user(user: User):
    # declare variables
    # formatting user to a dict
    # append dict to list users
    new_user = {
        "id": str(uuid.uuid4()),
        "username": user.username,
        "email": user.email
    }
    users.append(new_user)
    return new_user, 201
    

@app.get("/users/{user_id}")
def get_user(user_id: str):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"message": "User not found"}

@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    for u in users:
        if u["id"] == user_id:
            u["username"] = user.username
            u["email"] = user.email
            return u, 201
    return {"message": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            users.pop(i)
            return 201
    return {"message": "User does not exist"}
            

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)    
