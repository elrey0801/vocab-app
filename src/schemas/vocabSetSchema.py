from pydantic import BaseModel

class VocabSet(BaseModel):
    userId: int
    vocabSetName: str
    class Config:
        from_attributes = True