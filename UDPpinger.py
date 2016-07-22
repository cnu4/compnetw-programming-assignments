#!/usr/bin/python
import time
from socket import *

serverPort = 12000
serverName = '127.0.0.1'

clientSocket = socket(AF_INET, SOCK_DGRAM)
# set connection timeout
clientSocket.settimeout(1)

for i in range(1, 11):
	message = 'Ping %d %s' % (i, time.time())
	print message
	t0 = time.time()
	clientSocket.sendto(message, (serverName, serverPort))
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print 'from', serverAddress, ":", modifiedMessage, 'time =', (time.time() - t0) * 1000, 'ms'
	except:
		print 'Request timed out'
clientSocket.close()