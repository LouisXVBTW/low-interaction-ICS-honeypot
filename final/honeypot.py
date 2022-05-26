import threading, os
from protocols.seimenss7 import *
from protocols.bacnet import *
from protocols.crimsonV3 import *
from protocols.dnp3 import *
from protocols.ethernetIP import *
from protocols.iec import *
from protocols.melsecQ import *
from protocols.modbus import *
from protocols.omronFINS import *
from protocols.pcWorks import *
from protocols.tridiumNiagraFox import *
#from protocols.sampleProtocol import *
from database.updateDB import main as runUpdate
import os
print(os.getcwd())
filename = os.getcwd()+'/dashboard'
print (filename)

SERVER = "127.0.0.1"

def main():
    #print (seimenss7("hello", "people"))
    launchProtocols(SERVER, getProtocols())
    thread = threading.Thread(target=runUpdate, args=())
    thread.daemon = True
    thread.start()
    thread2 = threading.Thread(target=runDash, args=())
    thread2.daemon = True
    thread2.start()


def getProtocols():
    path = os.path.dirname(__file__)
    print(path)
    try:
        return os.listdir(path+'/protocols/')
    except:
        return os.listdir('protocols')
def launchProtocols(SERVER, protocols):
    for i in protocols:
        if ".py" in i:
            if "__" not in i:
                thread = threading.Thread(target=eval(i[:-3]), args=[SERVER, i[:-3]])
                thread.start()

def runDash():
    os.system(f'cd {filename};uvicorn dashboard:app --reload')



if __name__ == "__main__":
    main()  
