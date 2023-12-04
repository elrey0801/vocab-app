from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from controllers import vocabController
from schemas import vocabSchema, userSchema
from middlewares.authMiddleware import checkAuthenticated
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

router = APIRouter()

# @router.post("/get-vocabs/", response_model=list[vocabSchema.Vocab], dependencies=[Depends(checkAuthenticated)])
@router.post("/get-vocabs/", response_model=list[vocabSchema.Vocab])
async def getVocabs(
        vocabSetDeital: vocabSchema.VocabSetID = None,
        authData: str = Depends(checkAuthenticated),
        vocabController = Depends(vocabController.VocabController) ):

    # try:
    #     return vocabController.VocabController.getVocabs(vocabSetDeital=vocabSetDeital, authData=authData)
    # except Exception as e:
    #     logger.error(e)
    #     raise HTTPException(status_code=404, detail="getVocabs failed:: error getting vocabs")
    return vocabController.getVocabs(vocabSetDeital=vocabSetDeital, authData=authData)


# @router.post("/get-vocabs/", response_model=list[vocabSchema.Vocab])
# async def getVocabs(
#         db: Session = Depends(getDB), 
#         vocabSetDeital: vocabSchema.VocabSetID = None,
#         authData: str = Depends(checkAuthenticated)):

#     try:
#         return vocabController.getVocabs(db=db, vocabSetDeital=vocabSetDeital, authData=authData)
#     except Exception as e:
#         logger.error(e)
#         raise HTTPException(status_code=404, detail="getVocabs failed:: error getting vocabs")


@router.post("/post-vocab/")
async def postVocab(
        db: Session = Depends(getDB), 
        vocab: vocabSchema.CreateVocab = None, 
        authData: str = Depends(checkAuthenticated)):

    try:
        return vocabController.postVocab(db=db, vocab=vocab, authData=authData)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="error create vocab")


@router.delete("/delete-vocab/")
async def deleteVocab(
        db: Session = Depends(getDB), 
        vocabId: vocabSchema.VocabID = None, 
        authData: str = Depends(checkAuthenticated)):

    try:
        return vocabController.deleteVocab(db=db, vocabId=vocabId, authData=authData)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="error delete vocab")


@router.post("/get-test/", response_model=list[vocabSchema.Vocab])
async def postGetTest(
    db: Session = Depends(getDB), 
    testDetail: vocabSchema.GetTestDetail = None, 
    authData: userSchema.AuthDetail = Depends(checkAuthenticated)):

    try:
        return vocabController.postGetTest(db=db, testDetail=testDetail, authData=authData)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail="error getting test")