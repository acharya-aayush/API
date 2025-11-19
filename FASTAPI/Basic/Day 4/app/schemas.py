from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class ProfileResponse(BaseModel):
    username: str
    email: str
