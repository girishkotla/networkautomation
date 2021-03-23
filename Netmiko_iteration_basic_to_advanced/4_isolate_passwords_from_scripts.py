from netmiko import ConnectHandler
import getpass

user_name = input("Enter SSH Username: ")
password = getpass.getpass()

with open('commands_file') as f:
	commands_to_send = f.read().splitlines()

with open('devices_ip_list') as f:
	devices_list = f.read().splitlines()

for dev in devices_list:
	print('connecting to device '+ dev)
	ip_address = dev
	ios_device = {
		'device_type' : 'cisco_ios',
		'ip' : ip_address,
		'username' : user_name,
		'password' : password
	}

	net_connect = ConnectHandler(**ios_device)
	output = net_connect.send_config_set(commands_to_send)
	print(output)
