from netmiko import ConnectHandler

switch_1 = {
	'device_type'='cisco_ios'
	'ip'='192.168.255.100'  #Replace this IP with your target
	'username'= 'girish'    #SSH username
	'password'= 'cisco'     #SSH password
}

net_connect = ConnectHandler(**switch_1)        #open SSH connection using ConnectHandler

output = net_connect.send_command('show interface brief')         #enable mode commands
print(output)


config_commands = ['int loop 0','ip address 1.1.1.1 255.255.255.0']     #Enter all global config commands
output = net_connect.send_config_set(config_commands)                   #Send the globalconfig commands via SSH ConnectHandler; send_config_set means global conifg mode commands
print(output)


for n in range (2,21):                  #create vlans from 2 to 20
	print("creating VLAN "+str(n)) 
	config_commands = ['vlan '+str(n),'name python_VLAN_'+str(n)]   #global config commands
	output = net_connect.send_config_set(config_commands)
	print(output)
