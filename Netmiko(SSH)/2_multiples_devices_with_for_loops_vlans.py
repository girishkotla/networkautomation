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


all_devices = [s2,s3,s4,s5,s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range(2,21):
        commands_config = ['vlan '+str(n),"name vlan_num_"+str(n)]
        output = net_connect.send_config_set(lines)
        print (output)