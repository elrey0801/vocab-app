from sqlalchemy import Column, Integer, String, Boolean
from configs.connectdb import Base
from configs.connectdb import engine
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(String(100), nullable=False)
    status = Column(Boolean, nullable=False, server_default='0')
    vocab_sets = relationship('VocabSet', back_populates='user')

# Base.metadata.create_all(bind=engine)
