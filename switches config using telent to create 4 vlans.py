import getpass
import telnetlib


HOST = input("Enter the IP address of the Device to Telenet: ")
user = input("Enter the telnet username: ")
password = getpass.getpass()

tn=telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii')+b"\n")

if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii')+b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"config terminal\n")
tn.write(b"vlan 10\n")
tn.write(b"name python_vlan10\n")	#This is meanual method, using loops is recommended and will see that in the next upcomming codes
tn.write(b"vlan 20\n")
tn.write(b"name python_vlan20\n")
tn.write(b"vlan 30\n")
tn.write(b"name python_vlan30\n")
tn.write(b"vlan 40\n")
tn.write(b"name python_vlan40\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
