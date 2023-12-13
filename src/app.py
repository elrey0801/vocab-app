from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from routers import vocabRoute, webRoute, authRoute, vocabSetRoute
from configs.connectdb import Base, engine
from fastapi.staticfiles import StaticFiles
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(vocabRoute.router)
app.include_router(webRoute.router)
app.include_router(authRoute.router)
app.include_router(vocabSetRoute.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/public", StaticFiles(directory="public"), name="public")

logger.info('==============================APP STARTED==============================')





