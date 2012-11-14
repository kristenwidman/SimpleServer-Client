#!/usr/bin/env python

#kristenwidman
#simple python client using sockets

import socket

HOST = '127.0.0.1'
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

data = 'this is a string. casing is important. maybe.\n'
s.sendall(data)
received = ''
while True:
    print 'receiving data'
    new = s.recv(5)
    if not new:
        break
    received += new

s.close()
print 'Received:', received
