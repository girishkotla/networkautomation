import getpass
import telnetlib

HOST = "localhost"
user = input("Enter Telnet Username: ")
password = getpass.getpass()

f=open("switches_list")

for IP in f:
	IP=IP.strip()
	print("Backing UP Switch with IP: "+(IP))
	HOST = IP

	tn = telnetlib.Telnet(HOST)

	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii')+b"\n")

	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii')+b"\n")

	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	tn.write(b"terminal length 0\n")  #Show the Complete Configuration without Breaks/Pauses on Cisco Router/Switches, ASA Firewall and WLC (Wireless LAN Controller)
	tn.write(b"show running-config\n")
	tn.write(b"exit\n")

	read_output = tn.read_all()
	save_output = open("Backup of: "+HOST,"w")	#creatng a new file; "w" is nothing but giving writing permission for the File created
	save_output.write(read_output.decode('ascii'))  #save the read_output to the file created
	save_output.write("\n")
	save_output.close		#close the file after writing(backing up)

	print(tn.read_all().decode('ascii'))  #displays all the commands for your reference
