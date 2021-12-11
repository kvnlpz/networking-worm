<!-- # networking-worm -->
Just a worm project for a class. 


Contributors: 
Kevin Lopez
Yujin Chung
Yu Li
Desirae Prather

<!-- # Install pip for python 3 VM instructions -->
how to set up Python3 in VMS

1. Check VM to make sure Network is set NAT
2. python --version if show 2.7 do step 3,4,5,6
3. sudo su (if asked for password put cpsc)
4. update-alternatives --install /usr/bin/python python /usr/bin/python3 1
5. python --version if show 3.x then proceed to next step otherwise message in discord
6. exit (to get out of root)
7. python --version
8. pip3 install -U pip setuptools
9. pip3 install paramiko netifaces python-nmap netinfo

repeat steps for the other 2 vm

<!-- # Execution Instructions -->
1. config router's ip and dhcp
2. Enter command "sh ip dhcp bind" into router until 3 ips show
3. Enter "dhcp" into PC1
4. Check to see that all of them have been assigned a ip address from dhcp
5. go to a Lubuntu vm
6. create a note and copy our code into it and save it as "worm.py" onto Desktop
7. open terminal 
8. enter "cp Desktop/worm.py /tmp"
9. enter "python3 /tmp/worm.py"
