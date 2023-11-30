from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from controllers import vocabController
from middlewares.authMiddleware import checkAuthenticated

router = APIRouter()

@router.post("/get-vocabs/")
async def getVocabs(db: Session = Depends(getDB), request: Request = None, authData: str = Depends(checkAuthenticated)):
    try:
        data = await request.json()
        return vocabController.getVocabs(db=db, data=data)
    except:
        raise HTTPException(status_code=404, detail="error getting vocabs")
    
@router.post("/post-vocab/")
async def postVocab(db: Session = Depends(getDB), request: Request = None, authData: str = Depends(checkAuthenticated)):
    try:
        data = await request.json()
        return vocabController.postVocab(db=db, data=data)
    except:
        raise HTTPException(status_code=404, detail="error create vocab")

@router.delete("/delete-vocab/")
async def deleteVocab(db: Session = Depends(getDB), request: Request = None, authData: str = Depends(checkAuthenticated)):
    try:
        data = await request.json()
        return vocabController.deleteVocab(db=db, data=data)
    except:
        raise HTTPException(status_code=404, detail="error delete vocab")

@router.get("/get-test/{numOfVocabs}")
async def postGetTest(numOfVocabs: int, db: Session = Depends(getDB), request: Request = None, authData: str = Depends(checkAuthenticated)):
    try:
        return vocabController.getTest(numOfVocabs=numOfVocabs, db=db, authData=authData)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail="error getting test")