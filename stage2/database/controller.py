from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
with open("../../conf.ini", "r" ) as foo:
    path = "sqlite:////"+foo.readline().split(':')[1]

engine = create_engine(path, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
