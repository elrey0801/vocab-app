from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
from configs.connectdb import Base
from configs.connectdb import engine
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=False, server_default='0')
    vocabs = relationship('Vocab', back_populates='user')

# Base.metadata.create_all(bind=engine)
