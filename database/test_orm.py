import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from database.config import DB_URL

engine = create_engine(DB_URL, echo=True, encoding='utf-8')
Base = declarative_base()


class User(Base):
    __tablename__ = "users"    
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    fullname = Column(String(10))
    nickname = Column(String(10))

Base.metadata.create_all(engine)