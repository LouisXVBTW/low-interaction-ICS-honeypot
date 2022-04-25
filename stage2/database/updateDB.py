
from itertools import count
from socket import IP_RETOPTS
from typing import KeysView
import models, time, threading
from controller import SessionLocal, engine
from app import addIpStats, addProtocolStats, insertGeoShodan
# get all unique ips and protocols
# use this list to count how many there are (protocols and ips)
# then check which ips dont have location data
# select amount allowed to check with the api of choice for location

# then check for those that dont have shodan data and do the same

# wait certain time, if there is no change then wait again and check, otherwise do process again 

# we are now removing all shodan mentions, no longer in prod.

def main() -> None:

    while 1:
        time.sleep(30)
        for ip, icount in countIP(getIP()).items():
            addIpStats(ip, icount)
        
        for protocol, pcount in countProtocols(getPPROTOCOLS()).items():
            addProtocolStats(protocol, pcount)   
        getGeoIPS()
        time.sleep(30)
    
    
    
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
    
def getGeoIPS() -> list:
    igeo = []
    with SessionLocal.begin() as session:
        for c in session.query(models.IpStats).filter(models.IpStats.country == None):
            igeo.append(c.ip)
            print (c.ip, c.country)
    return igeo

    
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