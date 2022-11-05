
import socket			


s = socket.socket()		

port = 12345			

s.connect(('', port))

print (s.recv(1024).decode())
s.close()