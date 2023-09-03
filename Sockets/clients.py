import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.5.3.147',55555))
msg=s.recv(1024)
s.close()
print(msg.decode())