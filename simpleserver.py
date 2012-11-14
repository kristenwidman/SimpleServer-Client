#!/usr/bin/env python

#kristenwidman
#Nov 12, 2012

import socket
import string

HOST = '127.0.0.1'
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))
s.listen(1)
print 'Listening at host',HOST,'and port',PORT
data = ''
conn, sock_remote = s.accept()
while True:
    print 'Connected to',str(sock_remote)
    print 'Socket connects',conn.getsockname(),'to remote',conn.getpeername()
    new = conn.recv(5)
    if '\n' in new: #why does 'if not new:' not work here?
        break
    data += new
print 'Data received:',data

upper_data = string.upper(data)
conn.sendall(upper_data)
conn.close()

