import socket, threading
from socket import error as SocketError
import errno

port = 20547

class proCon0s:
	def __init__(self, SERVER, protocol):
		print (SERVER, protocol)
		ADDR = (SERVER, port) ## makes a tuple
		print (port, SERVER, ADDR)
		## creates server type (INET) and sock_stream
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(ADDR)
		server.listen()
		while True:
			## gets the data of the connector
			conn, addr = server.accept()
			## initiates thread to handle multiple connections
			thread = threading.Thread(target=self.handle_client, args=(conn, addr))
			thread.start()
			## prints out active connections to the thread
			print (f"[ACTIVE CONNECTIONS] {threading.activeCount() -1 }")

	#only running in threads
	def handle_client(self, conn, addr):
		print (f"[NEW CONNECTION] {addr} connected.")
		
		connected = True
		
		while connected:
			
			## awaits msg
			##welcome = b"Welcome to Linux machine\nThis is the thing"
			##conn.send(welcome)
			try:
				msg = conn.recv(1024).decode('latin-1')
		
				
				if msg:
					print(f"[{addr}] {msg}")
					conn.send(bytes(msg, 'utf-8'))
				if msg == "end":
					break
			except SocketError as e:	
				if e.errno == errno.ECONNRESET:

					print(" + Added to [POTENTIAL NMAP SCANNING]")

				raise e
			conn.close()
