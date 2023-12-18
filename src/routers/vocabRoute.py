from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from controllers.vocabController import VocabController
from schemas import vocabSchema, userSchema
from middlewares.authMiddleware import checkAuthenticated, checkAPIAuthenticated
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
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        response = vocabController.getVocabs(vocabSetId=vocabSetId, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="getVocabs failed:: error getting vocabs")


@router.post("/post-vocab")
async def postVocab(
        vocab: vocabSchema.CreateVocab = None, 
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        response = vocabController.postVocab(vocab=vocab, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="error create vocab")


@router.put("/update-vocab")
async def updateVocab(
        vocab: vocabSchema.Vocab = None, 
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        response = vocabController.updateVocab(vocab=vocab, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="error updating vocab")


@router.delete("/delete-vocab")
async def deleteVocab(
        vocabId: vocabSchema.VocabID = None, 
        authData: userSchema.AuthDetail = Depends(checkAPIAuthenticated),
        vocabController: VocabController = Depends()):

    try:
        response = vocabController.deleteVocab(vocabId=vocabId, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        logger.error(error)
        raise HTTPException(status_code=404, detail="error delete vocab")


@router.post("/get-test", response_model=list[vocabSchema.TestData])
async def postGetTest(
    testDetail: vocabSchema.TestDetail = None, 
    authData: userSchema.AuthDetail = Depends(checkAuthenticated),
    vocabController: VocabController = Depends()):

    try:
        response = vocabController.postGetTest(testDetail=testDetail, authData=authData)
        response = jsonable_encoder(response)
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response
    except HTTPException as error:
        logger.error(error.detail)
        raise error
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404, detail="error getting test")

@router.post("/get-test-all", response_model=list[vocabSchema.TestData])
async def postGetTest(
    numOfVocabs: vocabSchema.NumOfVocabs = None, 
    authData: userSchema.AuthDetail = Depends(checkAuthenticated),
    vocabController: VocabController = Depends()):

    # try:
    #     response = vocabController.postPracticeAll(numOfVocabs=numOfVocabs, authData=authData)
    #     response = jsonable_encoder(response)
    #     response = JSONResponse(content=response)
    #     response.set_cookie(key="access_token", value=authData.token, httponly=True)
    #     return response
    # except HTTPException as error:
    #     logger.error(error.detail)
    #     raise error
    # except Exception as error:
    #     print(error)
    #     raise HTTPException(status_code=404, detail="error getting test")

    response = vocabController.postPracticeAll(numOfVocabs=numOfVocabs, authData=authData)
    response = jsonable_encoder(response)
    response = JSONResponse(content=response)
    response.set_cookie(key="access_token", value=authData.token, httponly=True)
    return response