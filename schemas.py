from pydantic import BaseModel

class UserSignup(BaseModel):
    email: str
    password: str
    
class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class HabitCreate(BaseModel):
    name: str