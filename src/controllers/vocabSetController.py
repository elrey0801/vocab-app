from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from models import vocabSetModel
from schemas import vocabSetSchema, userSchema
from configs.connectdb import getDB
from utils import utils

class VocabSetController:
    def __init__(self, db: Session = Depends(getDB)):
        self.db = db

    def getVocabSets(self, authData: userSchema.AuthDetail):
        return self.db.query(vocabSetModel.VocabSet).filter(vocabSetModel.VocabSet.userId == authData.id).all()
        