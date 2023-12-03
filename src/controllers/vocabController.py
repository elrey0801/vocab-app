from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from models import vocabModel
from schemas import vocabSchema, userSchema
from configs.connectdb import engine
from utils import utils


def getVocabs(db: Session, authData: userSchema.AuthDetail = None):
    userId = authData.id
    if not userId:
        raise HTTPException(status_code=404, detail="userId is null")
    return db.query(vocabModel.Vocab).filter(vocabModel.Vocab.userId == userId).all()


def postVocab(db: Session, data = None): 
    item = vocabModel.Vocab(userId=data.get("userId"), word=data.get("word"), meaning=data.get("meaning"))
    db.add(item)
    db.commit()
    db.refresh(item)
    return JSONResponse(content={"message": "Vocab created:: ok"}, status_code=201)

def deleteVocab(db: Session, data = None):
    deleteVocabId = data.get("vocabId")
    deleteVocab= db.query(vocabModel.Vocab).filter(vocabModel.Vocab.id == deleteVocabId).first()
    db.delete(deleteVocab)
    db.commit()
    return JSONResponse(content={"message": "Vocab deleted:: ok"}, status_code=202)


def postGetTest(db: Session, testDetail: vocabSchema.TestDetail = None, authData: userSchema.AuthDetail = None):
    if testDetail.numOfVocabs < 5:
        return JSONResponse(
            content={"message": "Get test:: failed, you have to request at least 5 vocabs to make a test"}, 
            status_code=400)
    # checkAuthenticated => (access_token, user.id)
    userId = authData.id
    userVocabs = db.query(vocabModel.Vocab).filter(vocabModel.Vocab.userId == userId).all()
    if len(userVocabs) < 5:
        return JSONResponse(
            content={"message": "Get test:: failed, you need to create at least 5 vocabs to make a test"}, 
            status_code=400)

    if len(userVocabs) < testDetail.numOfVocabs:
        return JSONResponse(
            content={'message': f'Get test:: failed, only have {len(userVocabs)} vocabs (request {testDetail.numOfVocabs})'}, 
            status_code=400)

    familiarityWeight = [(11-vocab.familiarity) for vocab in userVocabs]
    returnVocabs = utils.randomUniqueChoices(userVocabs, familiarityWeight, testDetail.numOfVocabs)
    return returnVocabs
    