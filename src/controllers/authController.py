from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from models import userModel
from configs.connectdb import engine
import jwt, os
from dotenv import load_dotenv
from datetime import datetime, timedelta

dotenv_path = os.path.join(os.path.dirname(__file__), '..\..', '.env')
load_dotenv(dotenv_path)

SECURITY_ALGORITHM = os.getenv('SECURITY_ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = 1

def postLogin(db: Session, data = None):
    expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = data.copy()
    token.update({"exp": expires_delta})
    encoded_jwt = jwt.encode(token, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    response = JSONResponse(content="Login successful", status_code=200)
    response.set_cookie(key="access_token", value=encoded_jwt, httponly=True)
    return response