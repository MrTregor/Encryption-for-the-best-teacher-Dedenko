import socket
import random

from utils import power, p, g, port

s = socket.socket()
host = socket.gethostname()
s.connect((host, port))

b = random.randint(1, 10)
B = power(g, b, p)
s.send(str(B).encode())

A = int(s.recv(1024).decode())
skey = power(A, b, p)

message = "I speak only in English!"
message = "Братва, дельтуем в 20:30"
encrypted = ""
for i in message:
    encrypted += chr(ord(i) ^ skey)
print(f"Шифрую сообщение '{message}' > '{encrypted}'")
s.send(bytes(encrypted, 'utf-8'))
s.close()


