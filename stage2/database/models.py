from sqlalchemy import Boolean, Column, Integer, Sequence, String, Date, Float, BIGINT

from controller import Base

class Test1(Base):
    __tablename__ = "test1"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)

class ipLogs(Base):
    __tablename__ = "ipLogs"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    count = Column(String)


class logBacnet(Base):
    __tablename__ = "bacnet"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    port = Column(String, default="47808")
    ip = Column(String)
    raw = Column(String)