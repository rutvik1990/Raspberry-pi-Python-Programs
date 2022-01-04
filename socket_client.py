import socket
s = socket.socket()
host = socket.gethostname()
port = 12346

s.connect((host,port))
while True:
    data = raw_input("enter the data ypu wanr to send")
    s.send(data.encode())
    up = s.recv(1024).decode()
    print(up)

s.close()