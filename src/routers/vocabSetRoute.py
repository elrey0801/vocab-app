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