# Network Automation using PYTHON.

**TELNET:**

**NOTE:** Before automating using Telnet you first need to disable "TELNET" on switches.

Here are the **STEPS:** 

1. Give Username and password:

 SW(config)#username <enter_username> password <enter_pass>
 
 
2. Give enable password // the password that need to be entered while entering enable mode:

SW(config)# enable password/secret <enter_pass>

3. GIve an IP address to connect ussing telnet:

SW(config)# int vlan 1

SW(config-vlan)# ip address <IP_should_be_in_ubuntu_network> <subnet_mask>   //Enter **#ifconfig** in ubuntu to know the IP of container(ubuntu)

SW(config-vlan)# no sh

Sw(config-vlan)#exit


4. Open Tenelet to connect remotely:

SW(config)#line vty 0 4

SW(config-line)#login local

SW(config-line)#transport input telnet/ssh/all


**Recommendation:** Before directly executing code, check manually whether you are able to connect to the taget deivice using **TELNET.**


![image](https://user-images.githubusercontent.com/45974876/111051567-0afa8980-847a-11eb-9cc0-da2daba3bc02.png)

1. To create a LoopBack-0 and LoopBack-1 and assign IP's to them and exit from Telnet: https://github.com/girishkotla/networkautomation/blob/main/Create%20loopbacks%20in%20router(Basic).py
2. To cronfigure OSPF routing protocol for Router(R1): 
https://github.com/girishkotla/networkautomation/blob/main/Configure%20OSPF%20on%20router%20R1.py
3. Telnet to a switch(SW1) and create 4 VLANS (Vlan 10,20,30,40): https://github.com/girishkotla/networkautomation/blob/main/switches%20config%20using%20telent%20to%20create%204%20vlans.py

![image](https://user-images.githubusercontent.com/45974876/111139480-2fa04f80-85a7-11eb-8b80-01064a7f4627.png)


4. Configuring multiple switches using loops and opening file with the IP addresses:
https://github.com/girishkotla/networkautomation/tree/main/Telnet/Multiple_Switches_using_Loops
switches_list ==> have the list of IP addresses of the switches to configure. You can edit that file as per your Requirement
5. Backing UP multiple devices at one go and save the files of backups:
https://github.com/girishkotla/networkautomation/tree/main/Telnet/backup_configs_on_devices_using_telnet
After running the code when you check on the directory you can find some backup files.

