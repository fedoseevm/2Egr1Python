def f(x):
    return 14 - 3*x

# Przedzial a--b
# n - ilosc sekcji
def pros(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx + dx / 2) * dx
    return suma

print(pros(1, 4, 4))


def g(x):
    return -3*x - 2

def calka(p, k, n):
    dx = (k - p) / n
    suma = 0
    for i in range(n):
        suma += g(p + dx * i + dx / 2) * dx
    return suma

print(calka(-4, -1, 4))