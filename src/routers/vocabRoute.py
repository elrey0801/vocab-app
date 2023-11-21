from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from controllers import vocabController

router = APIRouter()

@router.post("/get-vocabs/")
async def getVocabs(db: Session = Depends(getDB), request: Request = None):
    try:
        data = await request.json()
        return vocabController.getVocabs(db=db, data=data)
    except:
        raise HTTPException(status_code=404, detail="error getting vocabs")
    
@router.post("/post-vocab/")
async def postVocab(db: Session = Depends(getDB), request: Request = None):
    try:
        data = await request.json()
        return vocabController.postVocab(db=db, data=data)
    except:
        raise HTTPException(status_code=404, detail="error create vocab")

@router.delete("/delete-vocab/")
async def deleteVocab(db: Session = Depends(getDB), request: Request = None):
    try:
        data = await request.json()
        return vocabController.deleteVocab(db=db, data=data)
    except:
        raise HTTPException(status_code=404, detail="error delete vocab")