from pydantic import BaseModel


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
    familiarity: int
    
class Vocab(VocabID, CreateVocab):
    pass

class GetTestDetail(BaseModel):
    numOfVocabs: int

