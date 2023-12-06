from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from models import vocabSetModel
from schemas import vocabSetSchema, userSchema
from configs.connectdb import getDB
from utils import utils
from utils.vocabUtils import VocabUtils

class VocabSetController(VocabUtils):
    def __init__(self, db: Session = Depends(getDB)):
        self.db = db

    def getVocabSets(self, authData: userSchema.AuthDetail):
        return self.db.query(vocabSetModel.VocabSet).filter(vocabSetModel.VocabSet.userId == authData.id).all()

    def postVocabSet(self, vocabSetDetail: vocabSetSchema.CreateVocabSet, authData: userSchema.AuthDetail):
        item = vocabSetModel.VocabSet(userId=authData.id, vocabSetName=vocabSetDetail.vocabSetName)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return JSONResponse(content={"message": "VocabSet created:: ok"}, status_code=201)
    
    def putVocabSet(self, vocabSetDetail: vocabSetSchema.VocabSet, authData: userSchema.AuthDetail):
        self.checkPosses(vocabSetDetail.id, authData)

        item = self.db.query(vocabSetModel.VocabSet).filter(vocabSetModel.VocabSet.id == vocabSetDetail.id)
        item.update({vocabSetModel.VocabSet.vocabSetName: vocabSetDetail.vocabSetName})

        self.db.commit()
        return JSONResponse(content={"message": "VocabSet updated:: ok"}, status_code=201)
    
    def deleteVocabSet(self, vocabSetDetail: vocabSetSchema.VocabSetID, authData: userSchema.AuthDetail):
        self.checkPosses(vocabSetDetail.id, authData)

        deleteVocabSet = self.db.query(vocabSetModel.VocabSet).filter(vocabSetModel.VocabSet.id == vocabSetDetail.id).first()
        self.db.delete(deleteVocabSet)
        self.db.commit()
        return JSONResponse(content={"message": "VocabSet deleted:: ok"}, status_code=202)
        