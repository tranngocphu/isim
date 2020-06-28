from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL

Session = sessionmaker(bind=create_engine(DB_URL))
session = Session()