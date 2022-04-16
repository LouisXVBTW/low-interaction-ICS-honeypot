import time
import socket
import unittest, io, warnings, threading
from unittest import mock
from sample_protocol import sampleProtocol

class testSampleProtocol(unittest.TestCase):
    def setUp(self) -> None:

        self.SERVER = "127.0.0.1"
        self.PORT = 1338
        self.ADDR = (self.SERVER, self.PORT)
        #with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            #   
         #   sampleProtocol.forTest(SERVER)
        #assert fake_stdout.getvalue() == f"[Generating Protocol on {ADDR}]\n"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server.bind(self.ADDR) #creates the protocol on the SERVER + PORT
        self.server.listen()

        
    def tearDown(self) -> None:
        self.server.close()
        

    def test_serverReply(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(self.ADDR)
        conn, addr = self.server.accept()
        thread = threading.Thread(target=sampleProtocol.handle_client, args=(self, conn, addr))
        thread.start()
        time.sleep(0.2)
        self.s.sendall(bytes('Hello World', 'utf-8'))
        data = self.s.recv(1024).decode('latin-1')
        self.s.sendall(bytes('end', 'utf-8'))
        self.s.close()
        print ("it got to the end")
        self.assertEqual(data, "HelloWorld")
