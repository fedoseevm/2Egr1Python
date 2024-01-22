# Metoda bisekcji
def f(x):
   return x ** 2 - 8 * x + 12

def bisekcja(a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def bisekcja_2(a, b, n):
    for i in range(n):
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

print(bisekcja_2(-5, 50, 10))
