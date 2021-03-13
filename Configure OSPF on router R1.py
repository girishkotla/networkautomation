import getpass
import telnetlib

HOST = input("Enter the IP address of Telnet connection: ") #Enter IP adress of target
user = input("Enter Telnet USERNAME: ")
password = getpass.getpass()


tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii')+b"\n")
#NOTE: The b indicates a bytes literal. All those string.encode(“ascii”) calls are converting str to ASCII-encoded bytes so that they can be concatenated with the bytes literal... this is all because ultimately the Telnet protocol expects ASCII-encoded bytes to be transmitted and received.

if password:
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii')+b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")		#Password for ENABLE mode
tn.write(b"config terminal\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.0 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
#Above line will display all the commands that gave in the program to visualize the commands