import socket, threading
from stem import SocketError
PORT = 1337

class sampleProtocol:
        
    def __init__(self, SERVER) -> None: #Server being localhost or 0.0.0.0
        ADDR = (SERVER, PORT)
        print (f"[Generating Protocol on {ADDR}]")
        #Generates TCP/IP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server.bind(ADDR) #creates the protocol on the SERVER + PORT
        server.listen()
        
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print (f"[ACTIVE CONNECTIONS] {threading.activeCount()}")
            
    def handle_client(self, conn, addr):
        
        print (f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
			
			## awaits msg
            
            try:
                msg = conn.recv(1024).decode('latin-1')
            except SocketError as e:
                print (e)
            if msg:
                print(f"[{addr}] {msg}")
            conn.send(bytes("HelloWorld", 'utf-8'))

            if msg == "end":
                connected = False
                conn.close()