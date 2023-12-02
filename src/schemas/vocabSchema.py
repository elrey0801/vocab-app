from pydantic import BaseModel


class Vocab(BaseModel):
    id: int
    userId: int
    word: str
    meaning: str
    example: str | None = None
    familiarity: int

    class Config:
        from_attributes = True