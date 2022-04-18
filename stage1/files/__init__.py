import unittest, threading, socket
from protocols.sampleProtocol import sampleProtocol



class testSampleProtocol(unittest.TestCase):
def setUp(self) -> None:
self.SERVER = "127.0.0.1" #keep server running locally
self.PORT = 2001 #random unused port for testing
self.ADDR = (self.SERVER, self.PORT) #generate tuple
self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifies server type
self.server.bind(self.ADDR) #creates the protocol on the SERVER + PORT
self.server.listen()

def tearDown(self) -> None:
self.server.close()


def test_serverReply(self) -> None:
self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
self.s.connect(self.ADDR)
conn, addr = self.server.accept()
thread = threading.Thread(target=sampleProtocol.handle_client, args=(self, conn, addr))
thread.daemon = True
thread.start()
self.s.sendall(bytes('Hello World', 'utf-8'))
data = self.s.recv(1024).decode('latin-1')
self.s.sendall(bytes('end', 'utf-8'))
self.s.close()
print ("it got to the end")
-e import unittest, threading, socket
-e from protocols.sampleProtocol import sampleProtocol
-e
-e
-e
-e class testSampleProtocol(unittest.TestCase):
-e def setUp(self) -> None:
-e self.SERVER = "127.0.0.1" #keep server running locally
-e self.PORT = 2001 #random unused port for testing
-e self.ADDR = (self.SERVER, self.PORT) #generate tuple
-e self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifies server type
-e self.server.bind(self.ADDR) #creates the protocol on the SERVER + PORT
-e self.server.listen()
-e
-e def tearDown(self) -> None:
-e self.server.close()
-e
-e
-e def test_serverReply(self) -> None:
-e self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
-e self.s.connect(self.ADDR)
-e conn, addr = self.server.accept()
-e thread = threading.Thread(target=sampleProtocol.handle_client, args=(self, conn, addr))
-e thread.daemon = True
-e thread.start()
-e self.s.sendall(bytes('Hello World', 'utf-8'))
-e data = self.s.recv(1024).decode('latin-1')
-e self.s.sendall(bytes('end', 'utf-8'))
-e self.s.close()
-e print ("it got to the end")
-e import unittest, threading, socket
-e from protocols.sampleProtocol import sampleProtocol
-e 
-e 
-e 
-e class testSampleProtocol(unittest.TestCase):
-e def setUp(self) -> None:
-e self.SERVER = "127.0.0.1" #keep server running locally
-e self.PORT = 2001 #random unused port for testing
-e self.ADDR = (self.SERVER, self.PORT) #generate tuple
-e self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifies server type
-e self.server.bind(self.ADDR) #creates the protocol on the SERVER + PORT
-e self.server.listen()
-e 
-e def tearDown(self) -> None:
-e self.server.close()
-e 
-e 
-e def test_serverReply(self) -> None:
-e self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
-e self.s.connect(self.ADDR)
-e conn, addr = self.server.accept()
-e thread = threading.Thread(target=sampleProtocol.handle_client, args=(self, conn, addr))
-e thread.daemon = True
-e thread.start()
-e self.s.sendall(bytes('Hello World', 'utf-8'))
-e data = self.s.recv(1024).decode('latin-1')
-e self.s.sendall(bytes('end', 'utf-8'))
-e self.s.close()
-e print ("it got to the end")
