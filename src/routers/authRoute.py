from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from configs.connectdb import getDB
from controllers import authController
from pydantic import BaseModel

router = APIRouter()

templates = Jinja2Templates(directory="views")

@router.get("/login", response_class=HTMLResponse)
async def getLogin(request: Request):
    # Truyền các biến cần thiết cho template
    context = {"request": request, "some_var": "some value"}
    # Trả về HTML view sử dụng Jinja2 template
    return templates.TemplateResponse("login.html", {"request": request, "messages": {"error": ""}})

@router.post("/login")
async def postLogin(db: Session = Depends(getDB), request: Request = None):
    try:
        data = await request.json()
        return authController.postLogin(db=db, data=data)
        # return templates.TemplateResponse("index.html", {"request": request})
        # return response

    except Exception as error:
        return templates.TemplateResponse("login.html", {"request": request, "messages": {"error": "Invalid Username or Password"}})