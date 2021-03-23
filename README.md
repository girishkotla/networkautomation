# Network Automation using PYTHON.

**TELNET:**

**NOTE:** Before automating using Telnet you first need to disable "TELNET" on switches.
Here you go: https://github.com/girishkotla/networkautomation/blob/main/Telnet/how_to_enable_telnet_on_network_device


**Recommendation:** Before directly executing code, check manually whether you are able to connect to the taget deivice using **TELNET.**


![image](https://user-images.githubusercontent.com/45974876/111051567-0afa8980-847a-11eb-9cc0-da2daba3bc02.png)

1. To create a LoopBack-0 and LoopBack-1 and assign IP's to them and exit from Telnet: https://github.com/girishkotla/networkautomation/blob/main/Telnet/Create%20loopbacks%20in%20router(Basic).py
2. To cronfigure OSPF routing protocol for Router(R1): 
https://github.com/girishkotla/networkautomation/blob/main/Telnet/Configure_OSPF_on_router_R1.py
3. Telnet to a switch(SW1) and create 4 VLANS (Vlan 10,20,30,40): https://github.com/girishkotla/networkautomation/blob/main/Telnet/switches%20config%20using%20telent_to_create_4_vlans.py

![image](https://user-images.githubusercontent.com/45974876/111139480-2fa04f80-85a7-11eb-8b80-01064a7f4627.png)


4. Configuring multiple switches using loops and opening file with the IP addresses:
https://github.com/girishkotla/networkautomation/tree/main/Telnet/Multiple_Switches_using_Loops
switches_list ==> have the list of IP addresses of the switches to configure. You can edit that file as per your Requirement
5. Backing UP multiple devices at one go and save the files of backups:
https://github.com/girishkotla/networkautomation/tree/main/Telnet/backup_configs_on_devices_using_telnet
After running the code when you check on the directory you can find some backup files.


**NETMIKO(SSH):**

**Network Design:**

![image](https://user-images.githubusercontent.com/45974876/111310493-271d4700-8683-11eb-8fd5-d3ef5766bfdf.png)

0. How to enable SSH, refer: https://github.com/girishkotla/networkautomation/blob/main/Netmiko(SSH)/multiple_switces_multiple_files_config/ssh_config.txt

**Recommended suggestion:** please check the SSH connection to the target(s), before automating.

1. Create loopbacks on a router using Netmiko(SSH): https://github.com/girishkotla/networkautomation/blob/main/Netmiko(SSH)/1_create_loopbacks_on_router.py
2. Configure multiples devices using for loops and create vlans on switche(s): https://github.com/girishkotla/networkautomation/blob/main/Netmiko(SSH)/2_multiples_devices_with_for_loops_vlans.py
3. Configure multiple devices(switches in this example) with opening/using multiple files which has global config commands: https://github.com/girishkotla/networkautomation/tree/main/Netmiko(SSH)/multiple_switces_multiple_files_config

For more examples refer: https://github.com/ktbyers/netmiko/tree/develop/examples
For full detailed information of Netmiko, refer: https://github.com/ktbyers/netmiko


**Iteration of NETMIKO (BASIC to ADVANCED):**
Here you go: https://github.com/girishkotla/networkautomation/tree/main/Netmiko_iteration_basic_to_advanced
You can find 6 files in this link.
> Start from the file-1 in-order and slowly, code will be improved by introducing many things...if you are properly following from the start..you will get know withot any discription. I haven't wrote any comments in the code this time. You can do add the comments....:-)
