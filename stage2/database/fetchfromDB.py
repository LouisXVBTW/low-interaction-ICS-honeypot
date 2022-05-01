import models
from controller import SessionLocal, engine


def read_protocols():

    with SessionLocal.begin() as session:
        out = session.query(models.ProtocolStats).all()
        return list(map(lambda x:{'protocol':x.protocol, 'protocolCount': x.protocolCount},out))
    

def read_ips():
    with SessionLocal.begin() as session:
       
        out = session.query(models.IpStats).all()
        return list(map(lambda x:{'ip':x.ip, 'ipCount': x.ipCount},out))
def read_geo():
    geo =[]
    with SessionLocal.begin() as session:
        out = session.query(models.IpStats).all()
        foo = list(map(lambda x:x.country, out))
        bar = list(map(lambda x:x.city, out))
        print(foo)
        print(bar)
    with SessionLocal.begin() as session:
        anotherout = session.query(models.AllInteractions).all()
    # COUNT ALL CITIES AND COUNTRIES HERE AND THEN RETURN IT
    return geo
if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    read_geo()
