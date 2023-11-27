from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from routers import userRoute, vocabRoute, webRoute, authRoute
from configs.connectdb import Base, engine
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)



app = FastAPI()
app.include_router(userRoute.router)
app.include_router(vocabRoute.router)
app.include_router(webRoute.router)
app.include_router(authRoute.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/public", StaticFiles(directory="public"), name="public")






