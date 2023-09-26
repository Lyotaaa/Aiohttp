from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from config_db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    ads = relationship("Ads", backref="user")


class Ads(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    creation_time = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("user.id"))
