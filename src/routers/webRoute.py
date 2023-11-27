from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from middlewares.authMiddleware import checkAuthenticated

router = APIRouter()

templates = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
async def getHomePage(request: Request, username: str = Depends(checkAuthenticated)):
    return templates.TemplateResponse("index.html", {"request": request, "username": username})