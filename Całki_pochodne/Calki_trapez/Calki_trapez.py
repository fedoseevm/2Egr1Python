def f(x):
    return x**(-2) + 2 * x

def calka(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx + dx) * dx
    return suma

print(calka(3, 6, 100))



def trapez(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += (f(a + i * dx) + f(a + i * dx + dx)) / 2 * dx
    return suma

print(trapez(3, 6, 3))

def trapez_2(a, b, n):
    dx = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * dx)
    return suma / 2 * dx

print(trapez_2(3, 6, 3))