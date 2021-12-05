<!-- # networking-worm -->
Just a worm project for a class. 

<!-- This was set up with the following Topology settings -->

Contributors: 
Kevin Lopez
Yujin C
Yu Li
Desirae Prather

conf t

int f0/1  

ip add 192.168.1.1 255.255.255.0  	

no shut 

int loop 0 

ip add 1.1.1.1 255.255.255.255

no shut

end

wr

show ip interface brief | exclude down 

conf t

service dhcp

ip dhcp pool BLUE 

lease 7 0 0    

network 192.168.1.0 255.255.255.0

default-router 192.168.1.1 

ip dhcp excluded-address 192.168.1.1 

exit

sh ip dhcp  bind