from netmiko import ConnectHandler

sw2 = {
	'device_type' : 'cisco_ios',
	'ip' : '192.168.255.10',
	'username' : 'girish',
	'password' : 'cisco'
}

net_connect = ConnectHandler(**sw2)
output = net_connect.send_command('show ip int br')
print (output)

commands_config = ['vlan 10','name sales']
output = net_connect.send_config_set(commands_config)
print(output)