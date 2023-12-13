from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from models import userModel
from configs.connectdb import getDB
import jwt, os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import bcrypt
from schemas import userSchema
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '..\..', '.env')
load_dotenv(dotenv_path)

SECURITY_ALGORITHM = os.getenv('SECURITY_ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = 1

class AuthController:
    def __init__(self, db: Session = Depends(getDB)):
        self.db = db

    def getNewToken(self, user):
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = {'username': user.username, 'password': user.password, "exp": expires_delta}
        encoded_jwt = jwt.encode(token, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
        return encoded_jwt

    def postLogin(self, authData: userSchema.UserLogin):
        user = self.db.query(userModel.User).filter(userModel.User.username == authData.username).first()
        if not user:
            logger.info(f'---No User found with this username:: {authData.username}')
            return JSONResponse(content="Login failed", status_code=401)
        if not bcrypt.checkpw(authData.password.encode('utf-8'), user.password.encode('utf-8')):
            logger.info('---User provided wrong password:: ' + user.username)
            return JSONResponse(content="Login failed", status_code=401)
        logger.info('---User logged in:: ' + user.username)

        
        encoded_jwt = self.getNewToken(user)
        # print('encoded token::', encoded_jwt)
        # print('decoded token::', jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[SECURITY_ALGORITHM]))
        response = JSONResponse(content="Login successful", status_code=200)
        response.set_cookie(key="access_token", value=encoded_jwt, httponly=True)
        return response

    def postLogout():
        pass