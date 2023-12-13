from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from fastapi.encoders import jsonable_encoder
from controllers.vocabSetController import VocabSetController
from schemas import vocabSetSchema, userSchema
from middlewares.authMiddleware import checkAuthenticated, checkAPIAuthenticated
from pydantic import ValidationError
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/get-vocabsets", response_model=list[vocabSetSchema.VocabSet])
async def getVocabSets(
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabSetController: VocabSetController = Depends()):

    try:
        response = vocabSetController.getVocabSets(authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="getVocabSets failed:: error getting vocabSets")
    
        
@router.post("/post-vocabset")
async def postVocabSet(
        vocabSetDetail: vocabSetSchema.CreateVocabSet,
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabSetController: VocabSetController = Depends()):

    try:
        response = vocabSetController.postVocabSet(vocabSetDetail=vocabSetDetail, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="postVocabSet failed:: error posting vocabSet")

@router.put("/update-vocabset")
async def putVocabSet(
        vocabSetDetail: vocabSetSchema.VocabSet,
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabSetController: VocabSetController = Depends()):

    try:
        response = vocabSetController.putVocabSet(vocabSetDetail=vocabSetDetail, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="updateVocabSet failed:: error updating vocabSet")


@router.delete("/delete-vocabset")
async def deleteVocabSet(        
        vocabSetDetail: vocabSetSchema.VocabSetID,
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabSetController: VocabSetController = Depends()):

    try:
        response = vocabSetController.deleteVocabSet(vocabSetDetail=vocabSetDetail, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="deleteVocabSet failed:: error deleting vocabSet")