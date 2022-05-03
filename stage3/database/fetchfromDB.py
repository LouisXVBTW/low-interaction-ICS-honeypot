import models
from controller import SessionLocal, engine
from sqlalchemy.sql import func

def read_protocols():

    with SessionLocal.begin() as session:
        out = session.query(models.ProtocolStats).order_by(models.ProtocolStats.protocolCount.desc()).limit(10)
        foo = list(map(lambda x:{'protocol':x.protocol, 'protocolCount': x.protocolCount},out))
        return foo

def read_ips():
    with SessionLocal.begin() as session:
       
        out = session.query(models.IpStats).all()
        foo = list(map(lambda x:{'ip':x.ip, 'ipCount': x.ipCount},out))
        top10 = list(map(lambda x: x.id, out))
        print(top10)
        otherCount = session.query(func.sum(models.IpStats.ipCount)).filter(models.IpStats.id.notin_(top10))
        if otherCount[0][0] != None:
            
            foo.append({'ip':'Other','ipCount':otherCount[0][0]})
        
        return foo


def read_geo():
    geo =[list(), list(), list(), list()]
    # need to get every unique country and then every ip with that country will supply their ip count and it will add up to total connections in a country
    # same with city 
    with SessionLocal.begin() as session:
        uniqueCountry = session.query(models.IpStats.country).distinct()
    allcountries=[]
    for i in uniqueCountry:

        with SessionLocal.begin() as session:
            countCountry = session.query(func.sum(models.IpStats.ipCount)).filter(models.IpStats.country ==i.country).all()
        allcountries.append({'country':i[0], 'count':countCountry[0][0]})
        # geo[0].append(i[0])
    sortedcountries = sorted(allcountries, key=lambda x: x['count'], reverse=True)
    if len(sortedcountries) > 10:
        for i in range(0,10):
            geo[0].append(sortedcountries[i]['country'])
            geo[1].append(sortedcountries[i]['count'])
        geo[0] = ["N/A" if v is None else v for v in geo[0]]
        with SessionLocal.begin() as session:
            otherCount = session.query(func.sum(models.IpStats.ipCount)).filter(models.IpStats.country.notin_(geo[0]))
        
        geo[0].append('Other')
        geo[1].append(otherCount[0][0])
    else:
        for i in range(0, len(sortedcountries)):
            geo[0].append(sortedcountries[i]['country'])
            geo[1].append(sortedcountries[i]['count'])
        geo[0] = ["N/A" if v is None else v for v in geo[0]]
        # geo[1].append(countCountry[0][0])
    # COUNT ALL CITIES AND COUNTRIES HERE AND THEN RETURN IT
    
    print(geo[0])
    print(geo[1])
    session.flush()
    with SessionLocal.begin() as session:
        uniqueCity = session.query(models.IpStats.city).distinct()
    allcities = []
    for i in uniqueCity:
        with SessionLocal.begin() as session:
            countCity = session.query(func.sum(models.IpStats.ipCount)).filter(models.IpStats.city ==i.city).all()
        allcities.append({'city':i[0], 'count':countCity[0][0]})
    sortedcities = sorted(allcities, key=lambda x: x['count'], reverse=True)
    if len(sortedcities) > 10:
        for i in range(0,10):
            geo[2].append(sortedcities[i]['city'])
            geo[3].append(sortedcities[i]['count'])
        geo[2] = ["N/A" if v is None else v for v in geo[2]]
        with SessionLocal.begin() as session:
            otherCount = session.query(func.sum(models.IpStats.ipCount)).filter(models.IpStats.city.notin_(geo[2]))
        geo[2].append('Other')
        geo[3].append(otherCount[0][0])
    else:
        for i in range(0,len(sortedcities)):
            geo[2].append(sortedcities[i]['city'])
            geo[3].append(sortedcities[i]['count'])
        geo[2] = ["N/A" if v is None else v for v in geo[2]]
    print(geo[2])
    print(geo[3])
    
    return geo
if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
