from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str
    class Config:
        from_attributes = True

class AuthDetail(UserLogin):
    id: int

