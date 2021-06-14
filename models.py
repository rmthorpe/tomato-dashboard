from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, REAL

Base = declarative_base()

class TomatoObj(Base):
    __tablename__ = 'tomCount'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    count = Column(Integer)

