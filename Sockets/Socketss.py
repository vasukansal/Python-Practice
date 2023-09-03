import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('10.5.3.147',55555))
s.listen()
while True:
    client,address=s.accept()
    print(f"connected to {address}")
    client.send("You are connected!!".encode())
    client.close()

