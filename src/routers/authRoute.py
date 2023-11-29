from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from controllers import authController
from pydantic import BaseModel
from middlewares.authMiddleware import checkNotAuthenticated, checkValidToken

router = APIRouter()

templates = Jinja2Templates(directory="views")

@router.get("/login", response_class=HTMLResponse, dependencies=[Depends(checkNotAuthenticated)])
# @router.get("/login", response_class=HTMLResponse)
async def getLogin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "messages": {"error": ""}})

@router.post("/login", dependencies=[Depends(checkNotAuthenticated)])
async def postLogin(db: Session = Depends(getDB), request: Request = None):
    try:
        data = await request.json()
        return authController.postLogin(db=db, data=data)

    except Exception as error:
        return JSONResponse(content="Login failed", status_code=401)

# @router.post("/logout", dependencies=[Depends(checkValidToken)])
@router.post("/logout")
async def postLogout(db: Session = Depends(getDB), request: Request = None):  
    response = JSONResponse(content="Logout successful", status_code=200)
    response.delete_cookie('access_token')
    return response