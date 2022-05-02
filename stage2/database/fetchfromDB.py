import models
from controller import SessionLocal, engine
from sqlalchemy.sql import func

def read_protocols():

    with SessionLocal.begin() as session:
        out = session.query(models.ProtocolStats).all()
        return list(map(lambda x:{'protocol':x.protocol, 'protocolCount': x.protocolCount},out))
    

def read_ips():
    with SessionLocal.begin() as session:
       
        out = session.query(models.IpStats).all()
        return list(map(lambda x:{'ip':x.ip, 'ipCount': x.ipCount},out))
def read_geo():
    geo =[list(), list(), list(), list()]
    # need to get every unique country and then every ip with that country will supply their ip count and it will add up to total connections in a country
    # same with city 
    with SessionLocal.begin() as session:
        uniqueCountry = session.query(models.IpStats.country).distinct()
    for i in uniqueCountry:

        with SessionLocal.begin() as session:
            countCountry = session.query(func.sum(models.IpStats.ipCount)).filter(models.IpStats.country ==i.country).all()
        geo[0].append(i[0])
        
        geo[1].append(countCountry[0][0])
    # COUNT ALL CITIES AND COUNTRIES HERE AND THEN RETURN IT
    geo[0] = ["N/A" if v is None else v for v in geo[0]]
    print(geo[0])
    session.flush()
    with SessionLocal.begin() as session:
        uniqueCity = session.query(models.IpStats.city).distinct()
    for i in uniqueCity:
        with SessionLocal.begin() as session:
            countCity = session.query(func.sum(models.IpStats.ipCount)).filter(models.IpStats.city ==i.city).all()
        geo[2].append(str(i[0]))
        geo[3].append(countCity[0][0])
    geo[2] = ["N/A" if v is None else v for v in geo[2]]
    return geo
if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
