from netmiko import ConnectHandler

with open('commands_file') as f:
	commands_to_send = f.read().splitlines()

with open('device_list') as f:
	devices_list = f.read().splitlines()

for dev in devices_list:
	print ('connecting to device: '+ dev)
	ip_address_of_device = dev
	ios_device = {
		'device_type' : 'cisco_ios',
		'ip' : ip_address_of_device,
		'username' : 'girish',
		'password' : 'cisco'
	}

	net_connect = ConnectHandler(**ios_device)
	output = net_connect.send_config_set(commands_to_send)
	print(output)