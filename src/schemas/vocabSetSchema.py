from pydantic import BaseModel, validator
from fastapi import HTTPException

class VocabSetID(BaseModel):
    id: int

class CreateVocabSet(BaseModel):
    vocabSetName: str
    @validator('vocabSetName')
    def validateVocabSetName(cls, value):
        if len(value) == 0:
            raise HTTPException(status_code=422, detail="Create VocabSet:: failed, name cannot be blank")
        return value

class VocabSet(VocabSetID, CreateVocabSet):
    pass