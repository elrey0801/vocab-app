from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from models import vocabSetModel
from schemas import userSchema
from configs.connectdb import getDB

class VocabUtils:
    # Check vocab set belongs to the requesting user
    def checkPosses(self, vocabSetId: int, authData: userSchema.AuthDetail):
        thisVocabSet = self.db.query(vocabSetModel.VocabSet).filter(vocabSetModel.VocabSet.id == vocabSetId).first()
        if (thisVocabSet is None) or (thisVocabSet.userId !=  authData.id):
            raise HTTPException(status_code=404, detail=f"checkPosses failed:: user <{authData.username}> doesnt have such vocab set")