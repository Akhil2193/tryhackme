# Metasploit

## Basics
- msfconsole: The main CLI
- modules: exploits,scanners,playloads,etc.
- tools: stand-alone tools that will help vulenrability research, vulnerability assessment,or pentesting.

## Main Components
- **Auxiliary**: Any supporting module, such as scanners, crawlers and fuzzers, can be found here. 
- **Encoders**: Encoders will allow you to encode the exploit and payload in the hope that a signature-based antivirus solution may miss them. 
- **Evasion**: While encoders will encode the payload, they should not be considered a direct attempt to evade antivirus software. On the other hand, “evasion” modules will try that, with more or less success.
- **Exploits**: Exploits, neatly organized by target system.
- **NOPs**: NOPs (No OPeration) do nothing, literally. They are represented in the Intel x86 CPU family they are represented with 0x90, following which the CPU will do nothing for one cycle. They are often used as a buffer to achieve consistent payload sizes.
- **Payloads**: Payloads are codes that will run on the target system. You will see four different directories under payloads: adapters, singles, stagers and stages.
    - **Adapters**: An adapter wraps single payloads to convert them into different formats. For example, a normal single payload can be wrapped inside a Powershell adapter, which will make a single powershell command that will execute the payload.
    - **Singles**: Self-contained payloads (add user, launch notepad.exe, etc.) that do not need to download an additional component to run.
    - **Stagers**: Responsible for setting up a connection channel between Metasploit and the target system. Useful when working with staged payloads. “Staged payloads” will first upload a stager on the target system then download the rest of the payload (stage). This provides some advantages as the initial size of the payload will be relatively small compared to the full payload sent at once.
    - **Stages**: Downloaded by the stager. This will allow you to use larger sized payloads.

    Metasploit has a subtle way to help you identify single (also called “inline”) payloads and staged payloads.
    ```
    generic/shell_reverse_tcp
    windows/x64/shell/reverse_tcp
    ```
    Both are reverse Windows shells. The former is an inline (or single) payload, as indicated by the “_” between “shell” and “reverse”. While the latter is a staged payload, as indicated by the “/” between “shell” and “reverse”.

- **Post**: Post modules will be useful on the final stage of the penetration testing process listed above, post-exploitation.

## msfconsole

- Launch `msfconsole`
- Some Commands:
    ```
    ls
    show
    help
    back
    clear
    use
    set
    history
    info
    search

    # You can direct the search function using keywords such as type and platform. 
    search type:auxiliary telnet
    ```
## Working with Modules

Once you have entered the context of a module using the `use` command followed by the module name, as seen earlier, you will need to set parameters. The most common parameters you will use are listed below. Remember, based on the module you use, additional or different parameters may need to be set. It is good practice to use the `show options` command to list the required parameters.

All parameters are set using the same command syntax:
`set PARAMETER_NAME VALUE`

### Different command prompts:


    - The regular command prompt: You can not use Metasploit commands here.      
    
    root@ip-10-10-XX-XX:~#
     
    - The msfconsole prompt: msf6 (or msf5 depending on your installed version) is the msfconsole prompt. As you can see, no context is set here, so context-specific commands to set parameters and run modules can not be used here.       
    
    msf6 >

    - A context prompt: Once you have decided to use a module and used the set command to chose it, the msfconsole will show the context. You can use context-specific commands (e.g. set RHOSTS 10.10.x.x) here.
  
    msf6 exploit(windows/smb/ms17_010_eternalblue) >

    - The Meterpreter prompt: Meterpreter is an important payload we will see in detail later in this module. This means a Meterpreter agent was loaded to the target system and connected back to you. You can use Meterpreter specific commands here.

    meterpreter >

    - A shell on the target system: Once the exploit is completed, you may have access to a command shell on the target system. This is a regular command line, and all commands typed here run on the target system.
           
    C:\Windows\system32>

        
- `show options` to see the all the available parameters of a exploit.
- To set a value for a parameter use the `set` command. e.g. `set rhosts 10.10.165.39`
- Parameters often used: 
    - **RHOSTS:** “Remote host”, the IP address of the target system. A single IP address or a network range can be set. This will support the CIDR (Classless Inter-Domain Routing) notation (/24, /16, etc.) or a network range (10.10.10.x – 10.10.10.y). You can also use a file where targets are listed, one target per line using `file:/path/of/the/target_file.txt`.
    - RPORT: “Remote port”, the port on the target system the vulnerable application is running on.
    - PAYLOAD: The payload you will use with the exploit.
    - LHOST: “Localhost”, the attacking machine (your AttackBox or Kali Linux) IP address.
    - LPORT: “Local port”, the port you will use for the reverse shell to connect back to. This is a port on your attacking machine, and you can set it to any port not used by any other application.
    - SESSION: Each connection established to the target system using Metasploit will have a session ID. You will use this with post-exploitation modules that will connect to the target system using an existing connection.
- Can `unset` the parameters using the `unset` command. For unsetting all parameters use `unset all`.
- `setg` to set a parameter globally for all the modules.
- Clear the `setg` by using `unsetg`
- `exploit` or `run` to run the exploit. Can also pass a parameter `exploit -z` to run the exploit and background the session as soon as it opens.
- Some modules support the `check` option. This will check if the target system is vulnerable without exploiting it.
### Sessions

Once a vulnerability has been successfully exploited, a session will be created. This is the communication channel established between the target system and Metasploit.

- `background` or `ctrl+z` command to background the session prompt and go back to the msfconsole prompt.
- `sessions` to list all the existing sessions
- To interact with any session `session -i <session no.>`
