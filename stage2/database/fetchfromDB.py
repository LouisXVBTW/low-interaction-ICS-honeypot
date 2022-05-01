import models, random
from controller import SessionLocal, engine


def read_protocols():

    with SessionLocal.begin() as session:
        out = session.query(models.ProtocolStats).all()
        return list(map(lambda x:{'protocol':x.protocol, 'protocolCount': x.protocolCount},out))
    

def read_ips():
    with SessionLocal.begin() as session:
       
        out = session.query(models.IpStats).all()
        return list(map(lambda x:{'ip':x.ip, 'ipCount': x.ipCount},out))


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
