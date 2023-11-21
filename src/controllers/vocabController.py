from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from models import vocabModel
from configs.connectdb import engine

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
    
    

    