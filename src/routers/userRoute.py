from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import userController
from configs.connectdb import getDB

router = APIRouter()

@router.get("/users")
def getUsers(skip: int = 0, limit: int = 10, db: Session = Depends(getDB)):
    return userController.getUsers(db=db, skip=skip, limit=limit)
