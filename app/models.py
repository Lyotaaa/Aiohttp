import atexit
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    func,
    create_engine,
    ForeignKey,
)
from config_db import PG_DSN

engine = create_engine(PG_DSN)
atexit.register(engine.dispose)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class OwnerModel(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    ads = relationship("AdsModel", backref="owner")


class AdsModel(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    creation_time = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("owners.id"))


Base.metadata.create_all(engine)
