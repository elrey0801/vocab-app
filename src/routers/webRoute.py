from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from middlewares.authMiddleware import checkAuthenticated
from schemas import userSchema
from utils.vocabUtils import VocabUtils

router = APIRouter()

templates = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
async def getHomePage(request: Request, authData: userSchema.AuthDetail = Depends(checkAuthenticated)):
    response = templates.TemplateResponse("index.html", {"request": request, "username": authData.username})
    response.set_cookie(key="access_token", value=authData.token, httponly=True)
    return response

@router.get("/test", response_class=HTMLResponse)
async def getTestPage(request: Request, authData: userSchema.AuthDetail = Depends(checkAuthenticated)):
    response = templates.TemplateResponse("test.html", {"request": request, "username": authData.username})
    response.set_cookie(key="access_token", value=authData.token, httponly=True)
    return response

@router.get("/vocab-set", response_class=HTMLResponse)
async def getVocabSetPage(request: Request, authData: userSchema.AuthDetail = Depends(checkAuthenticated)):
    response =  templates.TemplateResponse("vocab-set.html", {"request": request, "username": authData.username})
    response.set_cookie(key="access_token", value=authData.token, httponly=True)
    return response

@router.get("/vocabs/{vocabSetId}", response_class=HTMLResponse)
async def getVocabPage(
        vocabSetId: int, 
        request: Request, 
        authData: userSchema.AuthDetail = Depends(checkAuthenticated),
        vocabUtils: VocabUtils = Depends()):

    try:
        vocabUtils.checkPosses(vocabSetId, authData)
    except:
        response = templates.TemplateResponse("vocab-set.html", {"request": request, "username": authData.username})
        response.set_cookie(key="access_token", value=authData.token, httponly=True)
        return response

    response = templates.TemplateResponse("vocabs.html", {"request": request, "username": authData.username, "vocabSetId": vocabSetId})
    response.set_cookie(key="access_token", value=authData.token, httponly=True)
    return response
