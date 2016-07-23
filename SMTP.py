#!/usr/bin/python
from socket import *
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

mailserver = "smtp.sina.com"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':
	print '250 reply not received from server.'

# authenticate
username = "fangxw1004@sina.com"
password = raw_input('Input password of the email: ')
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authCommand = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authCommand)
recv = clientSocket.recv(1024)
print recv.decode()

# Send MAIL FROM command and print server response.
fromCommand = 'MAIL FROM:fangxw1004@sina.com\r\n'
clientSocket.send(fromCommand)
recv = clientSocket.recv(1024)
print recv

# Send RCPT TO command and print server response
rcptCommand = 'RCPT TO:fangxw1004@163.com\r\n'
clientSocket.send(rcptCommand)
recv = clientSocket.recv(1024)
print recv

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand)
recv = clientSocket.recv(1024)
print recv

# Send message data.
data = 'From:fangxw1004@sina.com\r\nTo:fangxw1004@163.com\r\nSubject:Hello World\r\n' + msg
clientSocket.send(data)

# Message ends with a single period.
clientSocket.send(endmsg)
recv = clientSocket.recv(1024)
print recv

# Send QUIT command and get server response.
clientSocket.send('quit\r\n')
recv = clientSocket.recv(1024)
print recv