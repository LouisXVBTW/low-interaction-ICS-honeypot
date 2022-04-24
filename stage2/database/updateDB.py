
from itertools import count
from socket import IP_RETOPTS
import models, time, threading
from controller import SessionLocal, engine
from app import addIpStats, addProtocolStats, insertGeoShodan
# get all unique ips and protocols
# use this list to count how many there are (protocols and ips)
# then check which ips dont have location data
# select amount allowed to check with the api of choice for location

# then check for those that dont have shodan data and do the same

# wait certain time, if there is no change then wait again and check, otherwise do process again 


def main() -> None:

    for ip, icount in countIP(getIP()).items():
        addIpStats(ip, icount)
    
    for protocol, pcount in countProtocols(getPPROTOCOLS()).items():
        addProtocolStats(protocol, pcount)
       
    getGeo()
    getShodan()
## get functions    
def getIP() -> list:
    iips = []
    with SessionLocal.begin() as session:
        for c in session.query(models.AllInteractions.ip).distinct():
            iips.append(c.ip)
    return iips
def getPPROTOCOLS() ->list:
    iprotocols = []

    with SessionLocal.begin() as session:
        for c in session.query(models.AllInteractions.protocol).distinct():
            iprotocols.append(c.protocol)            
    return iprotocols
    
def getGeo() -> list:
    igeo = []
    with SessionLocal.begin() as session:
        for c in session.query(models.IpStats).filter(models.IpStats.country == None):
            igeo.append(c.ip)
            print (c.ip, c.country)
    return igeo

def getShodan() -> list:
    ishodan = []
    with SessionLocal.begin() as session:
        for c in session.query(models.IpStats).filter(models.IpStats.shodan == None):
            ishodan.append(c.ip)
            print (c.ip, c.shodan)
    return ishodan
    
#do functions
def countIP(iips):
    ipCounts = {}
    for i in iips:
        with SessionLocal.begin() as session:
            count = session.query(models.AllInteractions).filter(models.AllInteractions.ip==i).count()
            ipCounts[i] = count
    return ipCounts

def countProtocols(iprotocols):
    protocolsCount = {}
    for i in iprotocols:
        with SessionLocal.begin() as session:
            count = session.query(models.AllInteractions).filter(models.AllInteractions.protocol == i).count()
            protocolsCount[i] = count
    return protocolsCount       
     
if __name__ == "__main__":
    main()