from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from models import vocabModel
from configs.connectdb import engine
import random

def getVocabs(db: Session, data = None):
    userId = data.get("userId")
    if not userId:
        raise HTTPException(status_code=404, detail="userId is null")
    vocabs = db.query(vocabModel.Vocab).filter(vocabModel.Vocab.userId == userId).all()
    content = [{"vocabId": vocab.id,"word": vocab.word, "meaning": vocab.meaning, "familiarity": vocab.familiarity} for vocab in vocabs]
    return JSONResponse(content=content, status_code=200)


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


def randomUniqueChoices(population, weights, k):
    selectedSet = set()

    while len(selectedSet) < k:
        choices = random.choices(population, weights, k=k - len(selectedSet))
        selectedSet.update(choices)

    return list(selectedSet)

def getTest(numOfVocabs: int, db: Session, authData = None):
    if numOfVocabs < 5:
        return JSONResponse(
            content={"message": "Get test:: failed, you have to request at least 5 vocabs to make a test"}, 
            status_code=400)
    # checkAuthenticated => (access_token, user.id)
    userId = authData[1]
    userVocabs = db.query(vocabModel.Vocab).filter(vocabModel.Vocab.userId == userId).all()
    if len(userVocabs) < 5:
        return JSONResponse(
            content={"message": "Get test:: failed, you need to create at least 5 vocabs to make a test"}, 
            status_code=400)

    if len(userVocabs) < numOfVocabs:
        return JSONResponse(
            content={'message': f'Get test:: failed, only have {len(userVocabs)} vocabs (request {numOfVocabs})'}, 
            status_code=400)

    familiarityWeight = [(11-vocab.familiarity) for vocab in userVocabs]
    returnVocabs = randomUniqueChoices(userVocabs, familiarityWeight, numOfVocabs)
    # randomVocabId = random.sample(range(0, len(userVocabs)), numOfVocabs)
    # returnVocabs = [userVocabs[i] for i in randomVocabId]
    content = [{"vocabId": vocab.id,"word": vocab.word, "meaning": vocab.meaning, "familiarity": vocab.familiarity} for vocab in returnVocabs]
    return JSONResponse(content=content, status_code=200)
    