from netmiko import ConnectHandler
import getpass
from netmiko.ssh_exception import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

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
	try:
		net_connect = ConnectHandler(**ios_device)
	except (AuthenticationException):
		print('Authentication Failuer for: '+ip_address)
		continue
	except (NetmikoTimeoutException):
		print('Timeout to device: '+ip_address)
		continue
	except(EOFError):
		print('End of file while attepting the device: '+ip_address)
		continue
	except(SSHException):
		print('SSH issue, Is SSH enabled? Check it for: '+ ip_address)
		continue
	except Exception as unknown_error:
		print('Some other Error: '+unkwown_error)
		continue

	output = net_connect.send_config_set(commands_to_send)
	print(output)
