from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from configs.connectdb import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)