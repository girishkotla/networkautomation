from netmiko import ConnectHandler

s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.20',
    'username': 'girish',
    'password': 'cisco',
}

s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.30',
    'username': 'girish',
    'password': 'cisco',
}

s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.40',
    'username': 'girish',
    'password': 'cisco',
}

s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.50',
    'username': 'girish',
    'password': 'cisco',
}

s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.60',
    'username': 'girish',
    'password': 'cisco',
}

with open('commands_core') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [s4,s5,s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('commands_access') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [s6,s5,s4,s3,s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
