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
 3. ubuntu@ubuntu:~$ pip3 install -U netmiko
 
 NOTE: if you are using soem shared hosting labs, this might not work. I tried in free-cml. It failed.
 
 
