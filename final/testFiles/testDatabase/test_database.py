import unittest, time
import sys, os

path = os.path.dirname(__file__)+'/../../database/'
print (path)
sys.path.append(path)
from controller import SessionLocal, engine
import models
from app import addIpStats, addProtocolStats, addAllInteractions, insertGeo


class testDatabase(unittest.TestCase):
    def setUp(self):
        self.idip = None
        self.idprotocol = None
        self.idall= None
        self.ip = "test.ip.com"
        self.protocol = "UnitTestingProtocol"
        self.country = "UnitedKingdom"
        self.city = "Portsmouth"
        self.date = "TestToday"
        self.time = ":time:"
        self.rawData = "RAWBEEF"
        addIpStats(self.ip, 1)
        addProtocolStats(self.protocol, 1)
        addAllInteractions(self.ip, self.protocol, self.date, self.time, self.rawData)
        

    def tearDown(self):
        with SessionLocal.begin() as session:
            session.query(models.IpStats).filter(models.IpStats.id == self.idip).delete()
            session.commit()
        with SessionLocal.begin() as session:
            session.query(models.ProtocolStats).filter(models.ProtocolStats.id == self.idprotocol).delete()
            session.commit()
        with SessionLocal.begin() as session:
            session.query(models.AllInteractions).filter(models.AllInteractions.ip == self.ip).delete()
            session.commit()

    def test_database_IpStats(self):
    
        with SessionLocal.begin() as session:
            for c in session.query(models.IpStats).filter(models.IpStats.ip == self.ip):
                self.idip = c.id
                self.assertEqual(c.ip, self.ip)
            
        insertGeo(self.ip, self.country, self.city)
        with SessionLocal.begin() as session:
            for c in session.query(models.IpStats).filter(models.IpStats.ip == self.ip):    
                self.assertEqual(c.country, self.country)
                self.assertEqual(c.city, self.city)
        # time.sleep(10)
    
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
