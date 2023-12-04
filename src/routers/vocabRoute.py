from fastapi import APIRouter, Depends, HTTPException
from controllers.vocabController import VocabController
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
        vocabController: VocabController = Depends()):

    try:
        return vocabController.getVocabs(vocabSetDeital=vocabSetDeital, authData=authData)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="getVocabs failed:: error getting vocabs")


@router.post("/post-vocab/")
async def postVocab(
        vocab: vocabSchema.CreateVocab = None, 
        authData: str = Depends(checkAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        return vocabController.postVocab(vocab=vocab, authData=authData)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="error create vocab")


@router.delete("/delete-vocab/")
async def deleteVocab(
        vocabId: vocabSchema.VocabID = None, 
        authData: str = Depends(checkAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        return vocabController.deleteVocab(vocabId=vocabId, authData=authData)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="error delete vocab")


@router.post("/get-test/", response_model=list[vocabSchema.Vocab])
async def postGetTest(
    testDetail: vocabSchema.TestDetail = None, 
    authData: userSchema.AuthDetail = Depends(checkAuthenticated),
    vocabController: VocabController = Depends()):

    try:
        return vocabController.postGetTest(testDetail=testDetail, authData=authData)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail="error getting test")