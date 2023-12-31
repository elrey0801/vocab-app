from fastapi import Depends, APIRouter, HTTPException, Cookie
from fastapi.responses import RedirectResponse
import jwt, os
from dotenv import load_dotenv
from models import userModel
from configs.connectdb import getDB
from sqlalchemy.orm import Session
import json
from datetime import datetime, timedelta
from schemas import userSchema
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

SECURITY_ALGORITHM = os.getenv('SECURITY_ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

def checkAuthenticated(db: Session = Depends(getDB), access_token: str = Cookie(None)):
    try:
        # print(jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM]))
        access_token = jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
    except jwt.ExpiredSignatureError:
        logger.info("Token has expired.")
        raise HTTPException(status_code=302, detail="Redirecting...", headers={"Location": "/login"})
    except jwt.InvalidTokenError:
        logger.info("Invalid token.")
        raise HTTPException(status_code=302, detail="Redirecting...", headers={"Location": "/login"})

    user = db.query(userModel.User).filter(userModel.User.username == access_token['username']).first()
    
    if (not user) or (user.password != access_token['password']):
        logger.info("Token is faked")
        raise HTTPException(status_code=302, detail="Redirecting...", headers={"Location": "/login"})
    
    expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token['exp'] = expires_delta
    newToken = jwt.encode(access_token, SECRET_KEY, algorithm=SECURITY_ALGORITHM)

    return userSchema.AuthDetail(id=user.id, username=access_token['username'], password=access_token['password'], token=newToken)


def checkNotAuthenticated(db: Session = Depends(getDB), access_token: str = Cookie(None)):
    try:
        access_token = jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
        user = db.query(userModel.User).filter(userModel.User.username == access_token['username']).first()
        if (not user) or (user.password != access_token['password']):
            return
    except jwt.ExpiredSignatureError:
        return
    except jwt.InvalidTokenError:
        return

    raise HTTPException(status_code=302, detail="Redirecting...", headers={"Location": "/"})


def checkValidToken(db: Session = Depends(getDB), access_token: str = Cookie(None)):
    try:
        jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
    except:
        raise HTTPException(status_code=302, detail="Redirecting...", headers={"Location": "/login"})

def checkAPIAuthenticated(db: Session = Depends(getDB), access_token: str = Cookie(None)):
    try:
        access_token = jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
    except jwt.ExpiredSignatureError:
        logger.info("Token has expired.")
        raise HTTPException(status_code=401, detail="Authentication failed:: Invalid token.")
    except jwt.InvalidTokenError:
        logger.info("Invalid token.")
        raise HTTPException(status_code=401, detail="Authentication failed:: Invalid token.")

    user = db.query(userModel.User).filter(userModel.User.username == access_token['username']).first()
    
    if (not user) or (user.password != access_token['password']):
        logger.info("Token is faked")
        raise HTTPException(status_code=401, detail="Authentication failed:: Invalid token.")

    expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token['exp'] = expires_delta
    newToken = jwt.encode(access_token, SECRET_KEY, algorithm=SECURITY_ALGORITHM)

    return userSchema.AuthDetail(id=user.id, username=access_token['username'], password=access_token['password'], token=newToken)