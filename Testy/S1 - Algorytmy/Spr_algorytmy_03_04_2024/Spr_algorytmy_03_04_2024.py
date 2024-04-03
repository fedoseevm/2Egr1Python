import math


def f(x):
    return x ** 4 / 500 - x ** 2 / 200 - 3 / 250

def g(x):
    return - x ** 3 / 30 + x / 20 + 1 / 6

def prostokatF(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx + dx / 2) * dx
    return suma

def prostokatG(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += g(a + i * dx + dx / 2) * dx
    return suma

# 70.1
zakup = (f(10) + abs(g(10))) * 8
#print(zakup)


#print(prostokatF(2,10, 1000))
#print(abs(prostokatG(2, 10, 1000)))

materialPozostaly = zakup - prostokatF(2,10, 1000) - abs(prostokatG(2, 10, 1000))
#print(round(materialPozostaly, 3))

# 70.2

def lamanaF(a, b, n):
    dx = (b - a) / n
    dlugosc = 0
    for i in range(1, n):
        dlugosc += math.sqrt(((f(a + i * dx) - f(a + i * dx - dx)) ** 2) - dx ** 2)
    return dlugosc

print(lamanaF(2, 10, 1000))

# 70.3
def prostokatEndF(a, b, n):
    dx = 0.25
    suma = 0
    for i in range(n, -1, - 1):
        suma += math.floor(f(a + i * dx))
    return suma

print(prostokatEndF(2, 10, 32))