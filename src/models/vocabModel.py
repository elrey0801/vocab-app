from sqlalchemy import Column, Integer, String, ForeignKey
from configs.connectdb import Base
from configs.connectdb import engine
from sqlalchemy.orm import relationship

class Vocab(Base):
    __tablename__ = 'vocabs'
    id = Column(Integer, primary_key=True, index=True)
    userId = Column('user_id', Integer, ForeignKey('users.id'))
    word = Column(String(50), nullable=False)
    meaning = Column(String(100), nullable=False)
    example = Column(String(1000))
    familiarity = Column(Integer, nullable=False, server_default='0')
    user = relationship('User', back_populates='vocabs')

# Base.metadata.create_all(bind=engine)
