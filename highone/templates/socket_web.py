#！usr/bin/env python
# -*- encoding= utf-8 -*-


import socket
import select

host = ''
port = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(host,port)
s.listen(5)
print 'begin...o'
while 1:
	infds,outfds,errfds = select.select([s,],[],[],5)

	if len(infds) != 0:
		clientsock,clientaddr = s.accept()
		infds_c,outfds_c,errfds_c = select.select([clientsock,],[],[],3)
		if len(infds_c)!=0:
			buf = clientsock.recv(8196)
			if len(buf) != 0:
				print buf
		clientsock.close()
		print 'clientsock_closed'
	print 'no data coming'