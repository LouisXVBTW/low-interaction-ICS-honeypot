from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
filename = os.path.dirname(__file__)+'/db.db'
print (filename)
with open(filename, "r" ) as foo:
    path = "sqlite:////"+filename

engine = create_engine(path, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
