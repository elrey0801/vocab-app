from pydantic import BaseModel


class CreateVocab(BaseModel):
    word: str
    meaning: str
    example: str | None = None
    familiarity: int
    
    class Config:
        from_attributes = True

class Vocab(CreateVocab):
    id: int


class TestDetail(BaseModel):
    numOfVocabs: int