# Python socket programming to archive TCP data from port 4713 with a static ip.
# this program dumps real time C37 data into a file c37day.txt
# written by Sai Akhil Reddy for the use in SICL lab at UCSD
# email: skonakal@ucsd.edu

import socket
import sys

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('172.17.69.20',4713)
print >>sys.stderr,'connecting to %s port %s' % server_address
tcpsock.connect(server_address)

#tcpsock.listen(1)


c37dat = open("c37dat.txt","w")

while True:
	print >>sys.stderr,'waiting for a connection'
#	connection, client_address = tcpsock.accept()

	try:
#		print >>sys.stderr,'connection from', client_address
		while True:
			data = tcpsock.recv(74)
			print >>sys.stderr,'receiving real-time C37 data' 
			if data:
#				print data
				c37dat.write("%s\n"%data)
			else:
#				print >>sys.stderr,'no more data from', client_address
				break
	finally:
		tcpsock.close()
c37dat.close()
