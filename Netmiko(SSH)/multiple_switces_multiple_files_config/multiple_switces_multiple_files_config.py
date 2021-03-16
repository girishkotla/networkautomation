from netmiko import ConnectHandler

sw2 = {
	'device_type' = 'cisco_ios',
	'ip' = '192.168.255.20',
	'username' = 'girish',
	'password' = 'cisco'
}

sw3 = {
	'device_type' = 'cisco_ios',
	'ip' = '192.168.255.30',
	'username' = 'girish',
	'password' = 'cisco'
}

sw4 = {
	'device_type' = 'cisco_ios',
	'ip' = '192.168.255.40',
	'username' = 'girish',
	'password' = 'cisco'
}

sw4 = {
	'device_type' = 'cisco_ios',
	'ip' = '192.168.255.50',
	'username' = 'girish',
	'password' = 'cisco'
}

sw4 = {
	'device_type' = 'cisco_ios',
	'ip' = '192.168.255.60',
	'username' = 'girish',
	'password' = 'cisco'
}

with open("commands_core") as f:
	lines = f.read().splitlines()
print(lines)

dev_list = [sw2,sw3,sw4]

for dev in dev_list:
	net_connect = ConnectHandler(**dev)

	output = net_connect.send_config_set(lines)
	print(output)

with open("Commans_access") as f:
	lines = f.read().splitlines()
print(lines)

dev_list = [sw6,sw5,sw4,sw3,sw2]

for dev in dev_list:
	net_connect = ConnectHandler(**dev)
	output = net_connect.send_config_set(lines)
	print(output)
