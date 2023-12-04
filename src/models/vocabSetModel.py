from sqlalchemy import Column, Integer, String, ForeignKey
from models.userModel import Base
from configs.connectdb import engine
from sqlalchemy.orm import relationship

class VocabSet(Base):
    __tablename__ = 'vocab_sets'
    id = Column(Integer, primary_key=True, index=True)
    userId = Column('user_id', Integer, ForeignKey('users.id'))
    vocabSetName = Column('vocab_set_name', String(50), nullable=False)
    user = relationship('User', back_populates='vocab_sets')
    vocabs = relationship('Vocab', back_populates='vocab_set')
    


# Base.metadata.create_all(bind=engine)
