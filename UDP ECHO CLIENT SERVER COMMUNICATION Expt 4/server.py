import socket
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
port=9999
s.bind(("localhost",port))

while True:
    data ,addr = s.recvfrom(1024)
    print(data.decode())