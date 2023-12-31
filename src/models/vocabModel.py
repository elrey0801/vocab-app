from sqlalchemy import Column, Integer, String, ForeignKey
from models.vocabSetModel import Base
from configs.connectdb import engine
from sqlalchemy.orm import relationship

class Vocab(Base):
    __tablename__ = 'vocabs'
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(100), nullable=False)
    meaning = Column(String(1000), nullable=False)
    example = Column(String(1000))
    familiarity = Column(Integer, nullable=False, server_default='0')
    vocabSetId = Column('vocab_set_id', Integer, ForeignKey('vocab_sets.id'))
    vocab_set = relationship('VocabSet', back_populates='vocabs')

# Base.metadata.create_all(bind=engine)
