from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from configs.connectdb import Base
from configs.connectdb import engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True)
    password = Column(String(50))

Base.metadata.create_all(bind=engine)
