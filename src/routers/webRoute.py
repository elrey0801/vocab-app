from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Khai báo thư mục templates để chứa file HTML
templates = Jinja2Templates(directory="views")

# Định nghĩa một route để hiển thị HTML view
@router.get("/", response_class=HTMLResponse)
async def getHomePage(request: Request):
    # Truyền các biến cần thiết cho template
    context = {"request": request, "some_var": "some value"}
    # Trả về HTML view sử dụng Jinja2 template
    return templates.TemplateResponse("index.html", {"request": request, "some_var": "some value"})