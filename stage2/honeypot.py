import threading, os
from files.protocols.seimenss7 import *
from files.protocols.bacnet import *
from files.protocols.crimsonV3 import *
from files.protocols.dnp3 import *
from files.protocols.ethernetIP import *
from files.protocols.iec import *
from files.protocols.melsecQ import *
from files.protocols.modbus import *
from files.protocols.omronFINS import *
from files.protocols.pcWorks import *
from files.protocols.proCon0s import *
from files.protocols.tridiumNiagraFox import *
#from files.protocols.sampleProtocol import *

SERVER = "127.0.0.1"

def main():
    #print (seimenss7("hello", "people"))
    launchProtocols(SERVER, getProtocols())

def getProtocols():
    return os.listdir(os.getcwd()+'/files/protocols/')

def launchProtocols(SERVER, protocols):
    for i in protocols:
        if ".py" in i:
            if "__" not in i:
                thread = threading.Thread(target=eval(i[:-3]), args=[SERVER, i[:-3]])
                thread.start()


def checkDB():
    pass

def runDash():
    pass

def exportCowrie():
    pass

if __name__ == "__main__":
    main()  
