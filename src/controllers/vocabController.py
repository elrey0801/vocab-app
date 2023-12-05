from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from models import vocabModel, vocabSetModel
from schemas import vocabSchema, userSchema
from configs.connectdb import getDB
from utils import utils
from utils.vocabUtils import VocabUtils

class VocabController(VocabUtils):
    def __init__(self, db: Session = Depends(getDB)):
        self.db = db

    def getVocabs(self, vocabSetDeital: vocabSchema.VocabSetID, authData: userSchema.AuthDetail = None):
        self.checkPosses(vocabSetId=vocabSetDeital.vocabSetId, authData=authData)
        return self.db.query(vocabModel.Vocab).filter(vocabModel.Vocab.vocabSetId == vocabSetDeital.vocabSetId).all()


    def postVocab(self, vocab: vocabSchema.CreateVocab, authData: userSchema.AuthDetail = None): 
        self.checkPosses(vocabSetId=vocab.vocabSetId, authData=authData)
        item = vocabModel.Vocab(
            word=vocab.word, 
            meaning=vocab.meaning, 
            example=vocab.example, 
            familiarity=vocab.familiarity,
            vocabSetId=vocab.vocabSetId)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return JSONResponse(content={"message": "Vocab created:: ok"}, status_code=201)


    def deleteVocab(self, vocabId: vocabSchema.VocabID, authData: userSchema.AuthDetail = None):
        self.checkPosses(vocabSetId=vocabId.vocabSetId, authData=authData)
        deleteVocab = self.db.query(vocabModel.Vocab).filter(vocabModel.Vocab.id == vocabId.id).first()
        self.db.delete(deleteVocab)
        self.db.commit()
        return JSONResponse(content={"message": "Vocab deleted:: ok"}, status_code=202)


    def postGetTest(self, testDetail: vocabSchema.TestDetail = None, authData: userSchema.AuthDetail = None):
        self.checkPosses(vocabSetId=testDetail.vocabSetId, authData=authData)
        vocabSet = self.db.query(vocabModel.Vocab).filter(vocabModel.Vocab.vocabSetId == testDetail.vocabSetId).all()
        if len(vocabSet) < 5:
            return JSONResponse(
                content={"message": "Get test:: failed, your set need to have at least 5 vocabs to make a test"}, 
                status_code=400)

        if len(vocabSet) < testDetail.numOfVocabs:
            return JSONResponse(
                content={'message': f'Get test:: failed, only have {len(vocabSet)} vocabs (request {testDetail.numOfVocabs})'}, 
                status_code=400)

        familiarityWeight = [(11-vocab.familiarity) for vocab in vocabSet]
        returnVocabs = utils.randomUniqueChoices(vocabSet, familiarityWeight, testDetail.numOfVocabs)
        return returnVocabs
    