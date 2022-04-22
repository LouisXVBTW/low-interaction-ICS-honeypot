import unittest, random
import sys, os
from requests import Session

from sqlalchemy import null
path = os.path.dirname(__file__)+'/../../database/'
print (path)
sys.path.append(path)
from controller import SessionLocal, engine
import models
from app import addIpStats, addProtocolStats, addAllInteractions, insertGeoShodan


class testDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.idip = None
        self.idprotocol = None
        self.idall= None
        self.ip = "test.ip.com"
        self.protocol = "UnitTestingProtocol"
        self.country = "United Kingdom"
        self.city = "Portsmouth"
        self.shodan = "Normal"
        self.time = ":time:"
        self.rawData = "RAWBEEF"
        addIpStats(self.ip, self.protocol)
        addProtocolStats(self.protocol)
        addAllInteractions(self.ip, self.time, self.rawData)
        
        # with SessionLocal.begin() as session:
        #     out1 = session.query(models.IpStats).all()
        #     print ("This liost",list(map(lambda x:print("IpStats",x.id, x.ip, x.ipCount, x.protocol, x.country, x.city, x.shodan),out1)))
        #     out2 = session.query(models.ProtocolStats).all()
        #     list(map(lambda x:print("ProtocolStats",x.id, x.protocol, x.protocolCount),out2))
        #     out3 = session.query(models.AllInteractions).all()
        #     list(map(lambda x:print("AllInteractions",x.id, x.ip, x.time, x.rawData),out3))
    def tearDown(self) -> None:
        with SessionLocal.begin() as session:
            session.query(models.IpStats).filter(models.IpStats.id == self.idip).delete()
            session.query(models.ProtocolStats).filter(models.ProtocolStats.id == self.idprotocol).delete()
            session.query(models.AllInteractions).filter(models.AllInteractions.ip == self.ip).delete()
            session.commit()

    def test_database_IpStats(self) -> None:
        
        with SessionLocal.begin() as session:
            for c in session.query(models.IpStats).filter(models.IpStats.ip == self.ip):
                self.idip = c.id
                self.assertEqual(c.ip, self.ip)
                self.assertEqual(c.protocol, self.protocol)
            
        insertGeoShodan(self.idip, self.country, self.city, self.shodan)
        with SessionLocal.begin() as session:
            for c in session.query(models.IpStats).filter(models.IpStats.ip == self.ip):    
                self.assertEqual(c.country, self.country)
                self.assertEqual(c.city, self.city)
                self.assertEqual(c.shodan, self.shodan)
        
    
    def test_database_ProtocolStats(self):
        
        with SessionLocal.begin() as session:
            for c in session.query(models.ProtocolStats).filter(models.ProtocolStats.protocol == self.protocol):
                self.idprotocol = c.id
                self.assertEqual(c.protocol, self.protocol)
                
    def test_database_AllInteractions(self):
        with SessionLocal.begin() as session:
            for c in session.query(models.AllInteractions).filter(models.AllInteractions.ip == self.ip):
                self.idall = c.id
                self.assertEqual(c.ip, self.ip)
                self.assertEqual(c.time, self.time)
                self.assertEqual(c.rawData, self.rawData)