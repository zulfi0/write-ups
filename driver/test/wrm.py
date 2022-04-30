import winrm

host = '10.10.11.106'
domain = 'DRIVER'
user = 'tony'
paswd = 'liltony'

s = winrm.Session(host,auth=('tony','liltony'))
r = s.run_cmd('whoami')

print(r.status_code)
print(r.std_out)
