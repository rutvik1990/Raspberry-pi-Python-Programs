import RPi. GPIO as GPIO
import time
import socket
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(False)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12346
s.bind((host,port))
s.listen(1)

while True:
    c, addr = s.accept()
    print(addr)
    data = c.recv(1024).decode()
    print(data)
    if data == "on":
        GPIO.output(12, True)
    if data == "off":
        GPIO.output(12, False)
    data = data.upper()
    c.send(data.encode())
    c.close()
s.close()
