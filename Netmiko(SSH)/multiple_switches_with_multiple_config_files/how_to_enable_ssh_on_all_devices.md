![image](https://user-images.githubusercontent.com/45974876/111308883-3bf8db00-8681-11eb-897a-3ba1b2d35e43.png)



!!! SW1:-

config terminal

!

ho sw1

!

int vlan 1

ip add 192.168.255.10 255.255.255.0

no sh

exit

!

username girish password cisco

enable password cisco

line vty 0 4

login local

transport input ssh

exit

!

!

!

ip domain-name devnetpython.com

crypto key generate rsa

1024

!

!

end

write


==========================================================================================================

!!!SW2:-

config terminal

!

ho sw2

!

int vlan 1

ip add 192.168.255.20 255.255.255.0

no sh

exit

!

username girish password cisco

enable password cisco

line vty 0 4

login local

transport input ssh

exit

!

!

!

ip domain-name devnetpython.com
crypto key generate rsa
1024
!
!
end
write

==========================================================================================================

!!!SW3:-


enable
!
config terminal
!
ho sw3
!
int vlan 1
ip add 192.168.255.30 255.255.255.0
no sh
exit
!
username girish password cisco
enable password cisco
line vty 0 4
login local
transport input ssh
exit
!
!
!
ip domain-name devnetpython.com
crypto key generate rsa
1024
!
!
end
write


==========================================================================================================

!!!!!!SW4:--

enable
!
config terminal
!
ho sw4
!
int vlan 1
ip add 192.168.255.40 255.255.255.0
no sh
exit
!
username girish password cisco
enable password cisco
line vty 0 4
login local
transport input ssh
exit
!
!
!
ip domain-name devnetpython.com
crypto key generate rsa
1024
!
!
end
write


==========================================================================================================


!!!!!SW5:-

enable
!
config terminal
!
ho sw5
!
int vlan 1
ip add 192.168.255.50 255.255.255.0
no sh
exit
!
username girish password cisco
enable password cisco
line vty 0 4
login local
transport input ssh
exit
!
!
!
ip domain-name devnetpython.com
crypto key generate rsa
1024
!
!
end
write

==========================================================================================================

!!!!!SW6:-

enable
!
config terminal
!
ho sw1
!
int vlan 1
ip add 192.168.255.10 255.255.255.0
no sh
exit
!
username girish password cisco
enable password cisco
line vty 0 4
login local
transport input ssh
exit
!
!
!
ip domain-name devnetpython.com
crypto key generate rsa
1024
!
!
end
write
