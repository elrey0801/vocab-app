from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from controllers.vocabSetController import VocabSetController
from schemas import vocabSetSchema, userSchema
from middlewares.authMiddleware import checkAuthenticated
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/get-vocabsets/", response_model=list[vocabSetSchema.VocabSet])
async def getVocabSets(
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabSetController = Depends(VocabSetController)):

    try:
        return vocabSetController.getVocabSets(authData=authData)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="getVocabSets failed:: error getting vocabSets")

@router.post("/post-vocabset/")
async def postVocabSet(
        vocabSetDetail: vocabSetSchema.CreateVocabSet,
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabSetController = Depends(VocabSetController)):

    try:
        return vocabSetController.postVocabSet(vocabSetDetail=vocabSetDetail, authData=authData)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="postVocabSet failed:: error posting vocabSet")

@router.put("/update-vocabset/")
async def putVocabSet(
        vocabSetDetail: vocabSetSchema.UpdateVocabSet,
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabSetController = Depends(VocabSetController)):

    try:
        return vocabSetController.putVocabSet(vocabSetDetail=vocabSetDetail, authData=authData)
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="updateVocabSet failed:: error updating vocabSet")


@router.delete("/delete-vocabset/")
async def deleteVocabSet(        
        vocabSetDetail: vocabSetSchema.VocabSetID,
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabSetController = Depends(VocabSetController)):

    try:
        return vocabSetController.deleteVocabSet(vocabSetDetail=vocabSetDetail, authData=authData)
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=404, detail="deleteVocabSet failed:: error deleting vocabSet")