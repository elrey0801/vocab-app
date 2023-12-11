from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from models import vocabModel, vocabSetModel
from schemas import vocabSchema, userSchema
from configs.connectdb import getDB
from utils import utils
from utils.vocabUtils import VocabUtils

class VocabController(VocabUtils):
    # def __init__(self, db: Session = Depends(getDB)):
    #     self.db = db

    def getVocabs(self, vocabSetId: int, authData: userSchema.AuthDetail):
        self.checkPosses(vocabSetId=vocabSetId, authData=authData)
        return self.db.query(vocabModel.Vocab).filter(vocabModel.Vocab.vocabSetId == vocabSetId).all()


    def postVocab(self, vocab: vocabSchema.CreateVocab, authData: userSchema.AuthDetail): 
        self.checkPosses(vocabSetId=vocab.vocabSetId, authData=authData)
        item = vocabModel.Vocab(
            word=vocab.word, 
            meaning=vocab.meaning, 
            example=vocab.example, 
            vocabSetId=vocab.vocabSetId)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return JSONResponse(content={"message": "Vocab created:: ok"}, status_code=201)


    def updateVocab(self, vocab: vocabSchema.Vocab, authData: userSchema.AuthDetail):
        self.checkPosses(vocabSetId=vocab.vocabSetId, authData=authData)
        updateVocab = self.db.query(vocabModel.Vocab).filter(vocabModel.Vocab.id == vocab.id)
        updateVocab.update({
            vocabModel.Vocab.vocabSetId: vocab.vocabSetId,
            vocabModel.Vocab.word: vocab.word,
            vocabModel.Vocab.meaning: vocab.meaning,
            vocabModel.Vocab.example: vocab.example,
            vocabModel.Vocab.familiarity: vocab.familiarity
        })
        self.db.commit()
        return JSONResponse(content={"message": "Vocab updated:: ok"}, status_code=201)


    def deleteVocab(self, vocabId: vocabSchema.VocabID, authData: userSchema.AuthDetail):
        self.checkPosses(vocabSetId=vocabId.vocabSetId, authData=authData)
        deleteVocab = self.db.query(vocabModel.Vocab).filter(vocabModel.Vocab.id == vocabId.id).first()
        self.db.delete(deleteVocab)
        self.db.commit()
        return JSONResponse(content={"message": "Vocab deleted:: ok"}, status_code=202)


    def postGetTest(self, testDetail: vocabSchema.TestDetail, authData: userSchema.AuthDetail):
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
        returnVocabsMeaning = set(m.meaning for m in returnVocabs)
        for r in returnVocabs:
            r.option = utils.makeOptions(returnVocabsMeaning, r.meaning)
        return returnVocabs
    