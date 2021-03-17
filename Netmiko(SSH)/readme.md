![image](https://user-images.githubusercontent.com/45974876/111310493-271d4700-8683-11eb-8fd5-d3ef5766bfdf.png)


**NOTE: **

**ubuntu@ubuntu:~$** python3 code1.py 
Traceback (most recent call last):
  File "code1.py", line 1, in <module>
    from netmiko import ConnectHandler
ModuleNotFoundError: No module named 'netmiko'

 You will get this error, because netmiko is the nodule that need to be inclused.
 
 Commands to run on your automation container: 
 
 1. ubuntu@ubuntu:~$ sudo apt-get update
 2. ubuntu@ubuntu:~$ sudo apt-get install python3-pip
 3. ubuntu@ubuntu:~$ sudo pip3 install -U netmiko 
 
 NOTE: if you are using soem shared hosting labs, this might not work. I tried in free-cml. It failed.
 
 **SOLUTION:**
 
 If you get the below error, the you need to update the pip3 setup tools.
 
 ERROR: 
 ModuleNotFoundError: No module named 'setuptools_rust' 
 (OR)
 Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-fkt2utq1/cryptography/

![image](https://user-images.githubusercontent.com/45974876/111459393-a290fe00-8740-11eb-9eb1-0415092e09b2.png)

**Run this command:** 

ubuntu@ubuntu:~$sudo pip3 install -U pip setuptools

**then run:** ubuntu@ubuntu:~$ sudo pip3 install -U netmiko     
(That should work)

**IF YOU ARE USING python version 2.0:**
**If you are using python 2.* then follow these commands to use NAPAML, NETMIKO:**

ubuntu@ubuntu:~$ sudo apt-get update

ubuntu@ubuntu:~$ sudo apt-get install python -y

ubuntu@ubuntu:~$ sudo apt-get install build-essential libssl-dev libffi-dev -y

ubuntu@ubuntu:~$ sudo apt-get install python-pip -y

ubuntu@ubuntu:~$ sudo pip install cryptography

ubuntu@ubuntu:~$ sudo pip install netmiko

ubuntu@ubuntu:~$ sudo pip install napalm
