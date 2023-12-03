from pydantic import BaseModel

class AuthDetail(BaseModel):
    id: int
    username: str | None = None
    password: str | None = None

    class Config:
        from_attributes = True