# import netifaces

from netifaces import interfaces, ifaddresses, AF_INET

import nmap
# initialize the port scanner
nmScan = nmap.PortScanner()

# scan localhost for ports in range 21-443
nmScan.scan('127.0.0.1', '21-4000')
nmScan.all_hosts()


# kevin
# interface = netifaces.interfaces()
# address = netifaces.ifaddresses(interface)



ip_list = []
for interface in interfaces():
	try:
		for link in ifaddresses(interface)[AF_INET]:
			ip_list.append(link['addr'])
			print(ip_list)
	
	except KeyError:
		print("(exception caught) there was an error that i'm ignoring lol")

# print(address)


# run a loop to print all the found result about the ports
for host in nmScan.all_hosts():
	print('the host : %s (%s)' % (host, nmScan[host].hostname()))
	print('state : %s' % nmScan[host].state())
	for proto in nmScan[host].all_protocols():
		print('Protocol : %s' % proto)
		lport = nmScan[host][proto].keys()
		# lport.sort()
		for port in lport:
			print ('pOrt : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))

# flag = True
# while(flag):
#	if os.path.exists(INFECTED_MARKER_FILE):
#		print("found the file")
#		flag = False
#	else:
#		print("file not found")
#		f = open(INFECTED_MARKER_FILE, "a")
#		f.write("filler text")
#		f.close()


