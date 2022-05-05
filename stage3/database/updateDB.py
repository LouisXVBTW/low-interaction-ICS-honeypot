import requests, json

import models, time, threading
from controller import SessionLocal, engine
from app import addIpStats, addProtocolStats, insertGeo
# get all unique ips and protocols |done|
# use this list to count how many there are (protocols and ips) |done|
# then check which ips dont have location data |done|
# select amount allowed to check with the api of choice for location

# sqlite> select protocolCount from protocolStats order by protocolCount desc limit 2;  
# 128
# 58
# sqlite>

# Get the ids too from the search and then stick them into this query
# sqlite> SELECT SUM(protocolCount) FROM protocolStats WHERE id != 11 AND id != 3;
# 332
# sqlite>

# which will give us the "other" count.

# wait certain time, if there is no change then wait again and check, otherwise do process again |done|

# we are now removing all shodan mentions, no longer in prod. 

def main() -> None:

    while 1:
        time.sleep(30)
        for ip, icount in countIP(getIP()).items():
            addIpStats(ip, icount)
        
        for protocol, pcount in countProtocols(getPPROTOCOLS()).items():
            addProtocolStats(protocol, pcount)   
        
        findGeo(getGeoIPS())
       
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

def getGeoIPS() -> list:
    igeo = []
    with SessionLocal.begin() as session:
        for c in session.query(models.IpStats).filter(models.IpStats.country == None).distinct():
            if c == None:
                return None
            igeo.append(c.ip)
            print (c.ip, c.country)
    
    return igeo

def findGeo(iips):
    if iips == None:
        pass
    for i in iips:
        url = 'http://ipwho.is/' + i 
        x = requests.get(url)
        response = x.content.decode().replace('"', '\"')
        d = json.loads(response)
        try:
            print(i)
            insertGeo(i, d['country'], d['city'])
        except:
            print('localhost')

if __name__ == "__main__":
    main()
    