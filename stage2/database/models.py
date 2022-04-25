from sqlalchemy import Boolean, Column, Computed, Integer, String

from controller import Base

class Test1(Base):
    __tablename__ = "test1"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)

class IpStats(Base):
    __tablename__ = "ipStats"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    ipCount = Column(Integer, default=1)
    country = Column(String)
    city = Column(String)

class ProtocolStats(Base):
    __tablename__ = "protocolStats"
    id = Column(Integer, primary_key=True, index=True)
    protocol = Column(String)
    protocolCount = Column(Integer, default=1)

class AllInteractions(Base):
    __tablename__ = "allInteractions"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    protocol = Column(String)
    date = Column(String)
    time = Column(String)
    rawData = Column(String)
    