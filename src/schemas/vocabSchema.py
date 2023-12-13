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
    @validator('word')
    def validateVocabSetName(cls, value):
        if len(value) == 0:
            raise HTTPException(status_code=422, detail="Create VocabSet:: failed, word cannot be blank")
        return value
    
    @validator('meaning')
    def validateVocabSetName(cls, value):
        if len(value) == 0:
            raise HTTPException(status_code=422, detail="Create VocabSet:: failed, meaning cannot be blank")
        return value
    
    
class Vocab(VocabID, CreateVocab):
    familiarity: int
    @validator('familiarity')
    def validateFamiliarity(cls, value):
        if value < 0 or value > 10:
            raise HTTPException(status_code=422, detail="Invalid Vocab data:: familiarity must be from 0 to 10")
        return value

class TestData(Vocab):
    option: list


class TestDetail(VocabSetID):
    numOfVocabs: int

    @validator('numOfVocabs')
    def validateNumOfVocabs(cls, value):
        if value < 5:
            raise HTTPException(status_code=422, detail="Get test:: failed, you have to request at least 5 vocabs to make a test")
        return value

