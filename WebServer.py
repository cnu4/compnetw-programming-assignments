#!/usr/bin/python
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(99)

while True:
	print 'ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		connectionSocket.send('HTTP/1.1 200 ok\r\n')
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		print '404 not found'
		connectionSocket.send('HTTP/1.1 404 Not Found')
		connectionSocket.close()
serverSocket.close()
