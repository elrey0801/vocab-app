from pydantic import BaseModel


class VocabSetID(BaseModel):
    vocabSetId: int
    class Config:
        from_attributes = True

class CreateVocab(VocabSetID):
    word: str
    meaning: str
    example: str | None = None
    familiarity: int
    
class Vocab(CreateVocab):
    id: int


class GetTestDetail(BaseModel):
    numOfVocabs: int

