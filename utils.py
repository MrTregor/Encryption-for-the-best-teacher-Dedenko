def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 1:
            x = (x * y) % c
        y = (y * y) % c
        b //= 2
    return x

p = 23
g = 5
port = 12345