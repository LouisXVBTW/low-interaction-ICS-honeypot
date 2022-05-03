import models, random
from controller import SessionLocal, engine



def addTest1(ititle, icomplete) -> None:
    with SessionLocal.begin() as session:

        new_item = models.Test1(title=ititle, complete=icomplete)
        session.add(new_item)
        session.commit()

def addIpStats(iip, icount):
    new = True
    with SessionLocal.begin() as session:
        
        for c in session.query(models.IpStats).filter(models.IpStats.ip == iip):
            c.ipCount = icount
            new = False

        if new:
            new_entry = models.IpStats(ip=iip, ipCount=icount)
            session.add(new_entry)
  
    session.commit()

def addProtocolStats(iprotocol, icount):
    new = True
    with SessionLocal.begin() as session:
        
        for c in session.query(models.ProtocolStats).filter(models.ProtocolStats.protocol == iprotocol):
            c.protocolCount = icount
            new = False

        if new:
            new_item = models.ProtocolStats(protocol=iprotocol, protocolCount=icount)
            session.add(new_item)
    session.commit()

def addAllInteractions(iip, iprotocol, idate, itime, irawData):
    with SessionLocal.begin() as session:
        new_item = models.AllInteractions(ip=iip, protocol=iprotocol, date=idate, time=itime, rawData=irawData)
        session.add(new_item)
        session.commit()

def insertGeo(iip, icountry, icity):
    with SessionLocal.begin() as session:
        for c in session.query(models.IpStats).filter(models.IpStats.ip == iip):
            c.country = icountry
            c.city = icity
        session.commit()

def add_DB():

    with SessionLocal.begin() as session:
        numb = str(random.randint(0,500))
        new_item = models.IpStats(protocol=numb)
        session.add(new_item)
        session.commit()

def read_DB():

    with SessionLocal.begin() as session:
        session.query(models.ProtocolStats).filter(models.ProtocolStats.id == 2).delete()
        out = session.query(models.ProtocolStats).all()
        testValue = list(map(lambda x:{'protocol':x.protocol, 'protocolCount': x.protocolCount},out))
        session.commit()

    return testValue

def main():
    models.Base.metadata.create_all(bind=engine)
    # add_DB()
    # addIpStats("TEST", "opopop")
    # addProtocolStats("53")
    # read_DB()

    # # drop_DB()

if __name__ == "__main__":
    print(engine.table_names())
    main()
