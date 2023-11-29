from fastapi import Depends, APIRouter, HTTPException, Cookie
from fastapi.responses import RedirectResponse
import jwt, os
from dotenv import load_dotenv
from models import userModel
from configs.connectdb import getDB
from sqlalchemy.orm import Session
import json

dotenv_path = os.path.join(os.path.dirname(__file__), '..\..', '.env')
load_dotenv(dotenv_path)

SECURITY_ALGORITHM = os.getenv('SECURITY_ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')

def checkAuthenticated(db: Session = Depends(getDB), access_token: str = Cookie(None)):
    try:
        # print(jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM]))
        access_token = jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        raise HTTPException(status_code=307, detail="Redirecting...", headers={"Location": "/login"})
    except jwt.InvalidTokenError:
        print("Invalid token.")
        raise HTTPException(status_code=307, detail="Redirecting...", headers={"Location": "/login"})

    user = db.query(userModel.User).filter(userModel.User.username == access_token['username']).first()
    
    if (not user) or (user.password != access_token['password']):
        print('Token is faked')
        raise HTTPException(status_code=307, detail="Redirecting...", headers={"Location": "/login"})

    return (access_token, user.id)


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

    raise HTTPException(status_code=307, detail="Redirecting...", headers={"Location": "/"})


def checkValidToken(db: Session = Depends(getDB), access_token: str = Cookie(None)):
    try:
        jwt.decode(access_token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
    except:
        raise HTTPException(status_code=307, detail="Redirecting...", headers={"Location": "/login"})