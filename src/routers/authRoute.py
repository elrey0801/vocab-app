from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from controllers.authController import AuthController
from middlewares.authMiddleware import checkNotAuthenticated
from schemas import userSchema

router = APIRouter()

templates = Jinja2Templates(directory="views")

@router.get("/login", response_class=HTMLResponse, dependencies=[Depends(checkNotAuthenticated)])
async def getLogin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "messages": {"error": ""}})


@router.post("/login", dependencies=[Depends(checkNotAuthenticated)])
async def postLogin(authData: userSchema.UserLogin, authController: AuthController = Depends()):
    try:
        return authController.postLogin(authData=authData)
    except Exception as error:
        print(error)
        return JSONResponse(content="Login failed", status_code=401)


@router.post("/logout")
async def postLogout(request: Request):  
    response = JSONResponse(content="Logout successful", status_code=200)
    response.delete_cookie('access_token')
    return response