import unittest, threading, socket
from sampleProtocol import sampleProtocol



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
        self.assertEqual(data, "Hello World")