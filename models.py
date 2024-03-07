from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
sessionmakeression = Session()
Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    user = Column(String(50))
    name = Column(String(50))
    passwd = Column(String(50))

Base.metadata.create_all(engine)