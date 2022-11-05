import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

s.sendto(bytes("Hola","utf-8"),("localhost",9999))