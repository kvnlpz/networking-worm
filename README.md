<!-- # networking-worm -->
Just a worm project for a class. 


Contributors: 
Kevin Lopez, 
Yujin Chung, 
Yu Li, 
Desirae Prather, 

<!-- # Install pip for python 3 VM instructions -->
How to set up Python3 in VMS:

1. Check VM to make sure Network is set NAT
2. open terminal
3. enter "python --version" if show version 2.7 do step 3,4,5,6
4. enter "sudo su" (if asked for password put cpsc)
5. enter "update-alternatives --install /usr/bin/python python /usr/bin/python3 1"
6. python --version if show 3.x then proceed to next step otherwise message in discord
7. enter "exit" (to get out of root)
8. enter "python --version" (check to see if it is now python 3.x)
9. enter "pip3 install -U pip setuptools"
10. enter "pip3 install paramiko netifaces python-nmap netinfo"
11. repeat steps for the other 2 vm

<!-- # Execution Instructions -->
How to execute worm.py with Python:

1. config router's ip and dhcp
2. Enter command "sh ip dhcp bind" into router until 3 ips show
3. Enter "dhcp" into PC1
4. Check to see that all of them have been assigned a ip address from dhcp
5. go to a Lubuntu vm
6. create a note and copy our code into it and save it as "worm.py" onto Desktop
7. open terminal 
8. enter "cp Desktop/worm.py /tmp" (Or just copy the worm.py from the Desktop folder to the tmp folder via copy & paste).
9. enter "python3 /tmp/worm.py" (Execute worm.py in the tmp folder. If location is in "/tmp" directory in terminal, enter "python3 worm.py" instead).
10. Check all tmp folders to see if the infected file spread. (Enter "ls /tmp" to check what's in the tmp directory). 
