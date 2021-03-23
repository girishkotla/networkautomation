from netmiko import ConnectHandler

with open('commands_file') as f:
	commands_to_send = f.read().splitlines()

sw1 = {
	'device_type' : 'cisco_ios',
	'ip'	: '192.168.255.10',
	'username' : 'girish',
	'password' : 'cisco'
}

sw2 = {
	'device_type' : 'cisco_ios',
	'ip'	: '192.168.255.20',
	'username' : 'girish',
	'password' : 'cisco'
}

dev_list = [sw1,sw2]

for dev in dev_list:
	net_connect = ConnectHandler(**dev)
	output = net_connect.send_config_set(commands_to_send)
	print(output)