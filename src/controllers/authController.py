from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from models import userModel
from configs.connectdb import engine
import jwt, os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import bcrypt

dotenv_path = os.path.join(os.path.dirname(__file__), '..\..', '.env')
load_dotenv(dotenv_path)

SECURITY_ALGORITHM = os.getenv('SECURITY_ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = 1

def postLogin(db: Session, data = None):
    user = db.query(userModel.User).filter(userModel.User.username == data['username']).first()
    if not user:
        print(f'No User found with this username:: {data["username"]}')
        return JSONResponse(content="Login failed", status_code=401)
    print('User logged in:: ', user.username)
    if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
        return JSONResponse(content="Login failed", status_code=401)

    expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = {'username': user.username, 'password': user.password, "exp": expires_delta}
    encoded_jwt = jwt.encode(token, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    # print('encoded token::', encoded_jwt)
    # print('decoded token::', jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[SECURITY_ALGORITHM]))
    response = JSONResponse(content="Login successful", status_code=200)
    response.set_cookie(key="access_token", value=encoded_jwt, httponly=True)
    return response

def postLogout(db: Session, data = None):
    pass