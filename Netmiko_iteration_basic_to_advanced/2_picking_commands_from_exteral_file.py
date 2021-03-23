from netmiko import ConnectHandler

with open('commands_for_switch') as f:
	commands_to_send = f.read().splitlines()

sw2 = {
	'device_type': 'cisco_ios',
	'ip' : '192.168.255.20',
	'username' : 'girish',
	'password' : 'cisco'
	}

net_connect = ConnectHandler(**sw2)
output = net_connect.send_config_set(lines)
print(output)