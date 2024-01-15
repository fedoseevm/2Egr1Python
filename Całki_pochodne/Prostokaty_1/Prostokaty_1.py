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
print(prostokaty_srodek(2,5,4))
print(prostokaty_poczatek(2,5,40))
print(prostokaty_koniec(2,5,400))
