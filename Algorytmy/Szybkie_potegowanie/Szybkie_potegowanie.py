# Szybkie potegowanie
# Iteracyjnie
def FastPow(a, n):
    wynik = 1
    while n > 0:
        if n % 2 == 1:
            wynik *= a
        a = a * a
        n = n // 2
    return wynik

#print(FastPow(2,9))

# Rekurencyjnie
def FastPowReku(a, n):
    if n == 0: return 1
    if n % 2 == 1:
        return FastPowReku(a * a, n // 2) * a
    return FastPowReku(a * a, n // 2)

print(FastPowReku(2, 7))