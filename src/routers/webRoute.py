from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from middlewares.authMiddleware import checkAuthenticated
from schemas import userSchema

router = APIRouter()

templates = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
async def getHomePage(request: Request, authData: userSchema.AuthDetail = Depends(checkAuthenticated)):
    return templates.TemplateResponse("index.html", {"request": request, "username": authData.username})

@router.get("/test", response_class=HTMLResponse)
async def getTestPage(request: Request, authData: userSchema.AuthDetail = Depends(checkAuthenticated)):
    return templates.TemplateResponse("test.html", {"request": request, "username": authData.username})

@router.get("/vocab-set", response_class=HTMLResponse)
async def getTestPage(request: Request, authData: userSchema.AuthDetail = Depends(checkAuthenticated)):
    return templates.TemplateResponse("vocab-set.html", {"request": request, "username": authData.username})