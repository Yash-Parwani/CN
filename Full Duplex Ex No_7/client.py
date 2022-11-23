from socket import *
HOST = 'localhost'                
PORT = 8000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
        message = input(">")             
        if message == '':
                break
        while message.lower() != 'go':
                message += '\r\n'
                tcpCliSock.send(message.encode())
                message = input(">")
                if message == '':
		                break
        else:                            
		        message = 'continue\r\n'
		        tcpCliSock.send(message.encode())
	    data = tcpCliSock.recv(BUFSIZ)
	    data = data.decode().strip()
	    if not data:
	           break
	    while data.lower() != 'continue':        
		        print(data)
		        data = tcpCliSock.recv(BUFSIZ)
		        data = data.decode().strip()
tcpCliSock.close()
