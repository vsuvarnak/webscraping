from sqlalchemy import create_engine, Column, String, Integer, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI

Base = declarative_base()

class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(255))
    site = Column(String(255))
    price = Column(String(255))
    scraped_at = Column(TIMESTAMP, server_default=func.now())

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
