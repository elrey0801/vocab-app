from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from controllers import vocabController
from schemas import vocabSchema, userSchema
from middlewares.authMiddleware import checkAuthenticated

router = APIRouter()

# @router.post("/get-vocabs/", response_model=list[vocabSchema.Vocab], dependencies=[Depends(checkAuthenticated)])
@router.get("/get-vocabs/", response_model=list[vocabSchema.Vocab])
async def getVocabs(db: Session = Depends(getDB), authData: str = Depends(checkAuthenticated)):
    try:
        return vocabController.getVocabs(db=db, authData=authData)
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

@router.post("/get-test/", response_model=list[vocabSchema.Vocab])
async def postGetTest(
    db: Session = Depends(getDB), 
    testDetail: vocabSchema.TestDetail = None, 
    authData: userSchema.AuthDetail = Depends(checkAuthenticated)):

    try:
        return vocabController.postGetTest(db=db, testDetail=testDetail, authData=authData)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail="error getting test")