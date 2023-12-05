from pydantic import BaseModel

class VocabSetID(BaseModel):
    id: int

class CreateVocabSet(BaseModel):
    vocabSetName: str

class VocabSet(VocabSetID, CreateVocabSet):
    pass

class UpdateVocabSet(VocabSetID):
    vocabSetNewName: str