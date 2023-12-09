from fastapi import APIRouter, Depends, HTTPException
from controllers.vocabController import VocabController
from schemas import vocabSchema, userSchema
from middlewares.authMiddleware import checkAuthenticated
from pydantic import ValidationError
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

router = APIRouter()

# @router.post("/get-vocabs/", response_model=list[vocabSchema.Vocab], dependencies=[Depends(checkAuthenticated)])
@router.get("/get-vocabs/{vocabSetId}", response_model=list[vocabSchema.Vocab])
async def getVocabs(
        vocabSetId: int,
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        return vocabController.getVocabs(vocabSetId=vocabSetId, authData=authData)
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="getVocabs failed:: error getting vocabs")


@router.post("/post-vocab")
async def postVocab(
        vocab: vocabSchema.CreateVocab = None, 
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        return vocabController.postVocab(vocab=vocab, authData=authData)
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="error create vocab")


@router.put("/update-vocab")
async def updateVocab(
        vocab: vocabSchema.Vocab = None, 
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        return vocabController.updateVocab(vocab=vocab, authData=authData)
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="error updating vocab")


@router.delete("/delete-vocab")
async def deleteVocab(
        vocabId: vocabSchema.VocabID = None, 
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        return vocabController.deleteVocab(vocabId=vocabId, authData=authData)
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="error delete vocab")


@router.post("/get-test", response_model=list[vocabSchema.Vocab])
async def postGetTest(
    testDetail: vocabSchema.TestDetail = None, 
    authData: userSchema.AuthDetail = Depends(checkAuthenticated),
    vocabController: VocabController = Depends()):

    try:
        return vocabController.postGetTest(testDetail=testDetail, authData=authData)
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail="error getting test")