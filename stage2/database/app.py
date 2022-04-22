import models, random
from controller import SessionLocal, engine



def addTest1(ititle, icomplete) -> None:
    with SessionLocal.begin() as session:

        new_item = models.Test1(title=ititle, complete=icomplete)
        session.add(new_item)
        session.commit()

def addIpStats(iip):
    new = True
    with SessionLocal.begin() as session:
        
        for c in session.query(models.IpStats).filter(models.IpStats.ip == iip):
            c.ipCount += 1
            new = False

        if new:
            new_entry = models.IpStats(ip=iip)
            session.add(new_entry)
  
        session.commit()

def addProtocolStats(iprotocol):
    new = True
    with SessionLocal.begin() as session:
        
        for c in session.query(models.ProtocolStats).filter(models.ProtocolStats.protocol == iprotocol):
            c.protocolCount += 1
            new = False

        if new:
            new_item = models.ProtocolStats(protocol=iprotocol)
            session.add(new_item)
        session.commit()

def addAllInteractions(iip, iprotocol, idate, itime, irawData):
    with SessionLocal.begin() as session:
        new_item = models.AllInteractions(ip=iip, protocol=iprotocol, date=idate, time=itime, rawData=irawData)
        session.add(new_item)
        session.commit()

def insertGeoShodan(iid, icountry, icity, ishodan):
    with SessionLocal.begin() as session:
        for c in session.query(models.IpStats).filter(models.IpStats.id == iid):
            c.country = icountry
            c.city = icity
            c.shodan = ishodan
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
        out = session.query(models.IpStats).all()
        print (out)
        list(map(lambda x:print("IpStats",x.id, x.ip, x.ipCount, x.protocol, x.country, x.city, x.shodan),out))
        session.commit()


        # list(map(lambda x:print(x.id, x.title,x.complete),out))
        # foo = list(map(lambda x:x.title,out))
        # print (foo)

# def drop_DB():
#     with SessionLocal.begin() as session:
#         session.drop(models.Test1)
#         session.commit()

def main():
    models.Base.metadata.create_all(bind=engine)
    # add_DB()
    # addIpStats("TEST", "opopop")
    addProtocolStats("53")
    read_DB()

    # # drop_DB()

if __name__ == "__main__":
    print(engine.table_names())
    main()
