from sqlalchemy.orm import Session
from models import userModel
from configs.connectdb import engine

def addUser(db: Session, username: str, password: str):
    db_item = userModel.User(username=name, password=password)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def getUsers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(userModel.User).offset(skip).limit(limit).all()