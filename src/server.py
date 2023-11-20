from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from configs.connectdb import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user.get_items(db=db, skip=skip, limit=limit)



