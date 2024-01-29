def f(x):
    return 2*x-1

def prostokaty_srodek(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx + dx / 2) * dx
    return suma

def prostokaty_poczatek(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx) * dx
    return suma

def prostokaty_koniec(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx + dx) * dx
    return suma


print(prostokaty_srodek(2,5,4))
print(prostokaty_poczatek(2,5,4))
print(prostokaty_koniec(2,5,4))
print("\n");

def trapez(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += (f(a + i * dx) + f(a + i * dx + dx)) / 2 * dx
    return suma

print(trapez(2, 5, 4))

def trapez_2(a, b, n):
    dx = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * dx)
    return suma / 2 * dx

print(trapez_2(2, 5, 4))
