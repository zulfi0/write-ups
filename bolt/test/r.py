import requests

url = "https://passbolt.bolt.htb:443/users/recover.json?api-version=v2"
url2 = "https://passbolt.bolt.htb:443/auth/verify?id=1cfcd300-0664-407e-85e6-c11664a7d86c"

body = '{"username":"eddie@bolt.htb"}'

headers = {"X-Csrf-Token":"7037f7e2c82707e7d2a87f37219554ce472c366a2781938fd189ebfd5bc6c41f70cc81bf52e91b09f719e6dc3e94faaf97b45417085768535114c4097eea8643","Content-Type":"application/json","Content-Length":"29","Cookie":"passbolt_session=2s1020mk4dh5hb5r986l7ksigh; csrfToken=7037f7e2c82707e7d2a87f37219554ce472c366a2781938fd189ebfd5bc6c41f70cc81bf52e91b09f719e6dc3e94faaf97b45417085768535114c4097eea8643","Accept":"application/json"}

#post 1
pos =  requests.post(
        url,
        data=body,
        headers=headers,
        verify=False
        )

print(pos.text)

req = requests.get(
        url2,
        headers=headers,
        verify=False
        )
print(req.text)

