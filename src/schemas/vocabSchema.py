from pydantic import BaseModel, validator
from fastapi import HTTPException


class VocabSetID(BaseModel):
    vocabSetId: int
    class Config:
        from_attributes = True

class VocabID(VocabSetID):
    id: int

class CreateVocab(VocabSetID):
    word: str
    meaning: str
    example: str | None = None
    
    
class Vocab(VocabID, CreateVocab):
    familiarity: int


class TestDetail(VocabSetID):
    numOfVocabs: int

    @validator('numOfVocabs')
    def validateNumOfVocabs(cls, value):
        if value < 5:
            raise HTTPException(status_code=422, detail="Get test:: failed, you have to request at least 5 vocabs to make a test")
        return value

