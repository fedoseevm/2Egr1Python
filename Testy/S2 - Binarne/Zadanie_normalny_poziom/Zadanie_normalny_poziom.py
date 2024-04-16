# 1. Napisz alg dodawania dwoch liczb binarnych o tej samej dlugosci.
def AddBinarySameLen():
    bin1 = str(input("Podaj perwsza liczbe binarna: "))
    bin2 = str(input("Podaj druga liczbe binarna: "))
    wynik = ""
    suma = 0
    for i in range(1, len(bin1) + 1):
        suma += int(bin1[-i]) + int(bin2[-i])
        wynik = str(suma % 2) + wynik
        suma = suma // 2
    if suma > 0:
        wynik = str(suma) + wynik

    #r = 0                                             # Rozwiazanie wersja 2
    #for i in range(len(bin1)):
    #    suma = int(bin1[-i-1]) + int(bin2[-i-1]) + r
    #    m = suma % 2
    #    r = suma // 2
    #    wynik = str(m) + wynik
    #if r > 0:
    #    wynik = str(r) + wynik
    return wynik
#print(AddBinarySameLen())

# 2. Napisz algorytm dodawania dwoch liczb binarnych o roznej dlugosci.
def AddBinaryDiffLen():
    bin1 = str(input("Podaj perwsza liczbe binarna: "))
    bin2 = str(input("Podaj druga liczbe binarna: "))
    if (len(bin1) > len(bin2)):
        roz = len(bin1) - len(bin2)
        bin2 = "0" * roz + bin2
        #while len(bin1) != len(bin2):      # Tak byloby w innych jezykach
        #    bin2 = "0" + bin2
    else:
        roz = len(bin2) - len(bin1)
        bin2 = "0" * roz + bin1

    wynik = ""
    suma = 0
    for i in range(1, len(bin1) + 1):
        suma += int(bin1[-i]) + int(bin2[-i])
        wynik = str(suma % 2) + wynik
        suma = suma // 2
    if suma > 0:
        wynik = str(suma) + wynik
    return wynik
#print(AddBinaryDiffLen())

# 3. Wypisz wszystkie liczby binarne szesciocyfrowe, w ktorych liczba jedynek jest 2 razy wieksza od liczby zer.
# 100111
# 101011
# 101101
# 101110
# 110011
# 110101
# 110110
# 111001
# 111010
# 111100
def zad3():
    for i in range(1, 5):
        liczba = list("111111")  # Konwertacja do listy, aby miec mozliwosc jej edycji
        liczba[i] = "0"
        for j in range(i+1, 6):
            liczba[j] = "0"
            print(''.join(liczba))  # Przeksztalcenie do stringa i wypisywanie
            liczba[j] = "1"  # Ustawie 1 zamiast 0, aby przy kolejner iteracji zera sie nie zostawaly
#zad3()


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

print(FastPow(2,9))


def FastPowReku(a, n):
    if n == 0: return 1
    if n % 2 == 1:
        return FastPowReku(a * a, n // 2) * a
    return FastPowReku(a * a, n // 2)

print(FastPowReku(2, 9))