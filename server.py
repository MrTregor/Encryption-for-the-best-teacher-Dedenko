import socket
import random

from utils import power, p, g, port


s = socket.socket()
host = socket.gethostname()

s.bind((host, port))

while True:
    s.listen(5)
    c, addr = s.accept()
    print("Подсоединился человечек: " + str(addr))

    a = random.randint(1, 10)
    A = power(g, a, p)
    c.send(str(A).encode())

    B = int(c.recv(1024).decode())
    skey = power(B, a, p)

    data = c.recv(1024).decode()
    print(f"Получил сообщение: '{data}'")
    decrypted = ""
    for i in data:
        decrypted += chr(ord(i) ^ skey)
    print(f"Расшифрованное сообщение: '{decrypted}'")
c.close()


