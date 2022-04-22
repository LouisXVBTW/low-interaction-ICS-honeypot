import sys, os
filename = os.path.dirname(__file__)+"/../database/"
sys.path.append(filename)
from app import addIpStats, addProtocolStats, addAllInteractions, insertGeoShodan

import errno
import socket, threading
from socket import error as SocketError
port = 502

class modbus:
	def __init__(self, SERVER, protocol):
		print (SERVER, protocol)
		ADDR = (SERVER, port) ## makes a tuple
		self.protocol = protocol		
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
		addIpStats(addr[0], self.protocol)
		
		connected = True
		
		while connected:
			
			## awaits msg
			##welcome = b"Welcome to Linux machine\nThis is the thing"
			##conn.send(welcome)
			try:
				msg = conn.recv(1024)
				hexOFmsg = msg.hex()
				msg = msg.decode("latin-1")
		
				
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
