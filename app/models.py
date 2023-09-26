from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from config_db import Base
from sqlalchemy.orm import relationship


class Acync_OwnerModel(Base):
    __tablename__ = "acync_owners"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    ads = relationship("Acync_AdsModel", backref="acync_owner")


class Acync_AdsModel(Base):
    __tablename__ = "acync_ads"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    creation_time = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("acync_owners.id"))


# Base.metadata.create_all(engine)
