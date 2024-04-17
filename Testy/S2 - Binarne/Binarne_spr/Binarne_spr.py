from tkinter import END


def DecToBin(n):
    binarna = ""
    while n > 0:
        binarna = str(n % 2) + binarna 
        n = n // 2
    return binarna

# Zadanie 1
def zadanie1(n):
    binarna = DecToBin(n)
    licznik = 1
    for i in range(len(binarna) - 1):
        if (binarna[i] != binarna[i + 1]):
            licznik += 1
    #if binarna[-1] != binarna[-2]:
    #    licznik +=1
    print(licznik)

#print(DecToBin(135))
#zadanie1(135)


# Zadanie 2
def CountBlocks(binarna):
    licznik = 1
    for i in range(len(binarna) - 1):
        if (binarna[i] != binarna[i + 1]):
            licznik += 1
    return licznik


def zadanie2():
    with open("bin.txt", "r") as file:
        T = file.read().split()

    licznik = 0
    for i in range(len(T)):
        if CountBlocks(T[i]) <= 2:
            licznik += 1
    print(licznik)
#zadanie2()


# Zadanie 3
def zadanie3():
    with open("bin.txt", "r") as file:
        T = file.read().split()

    longestBin = T[0]
    for i in range(1, len(T)):
        if len(T[i]) > len(longestBin):
            longestBin = T[i]

    for i in range(len(T)):
        if len(T[i]) < len(longestBin):
            T[i] = "0" * (len(longestBin) - len(T[i])) + T[i]

    maxBin = T[0]
    for i in range(1, len(T)):
        for j in range(len(longestBin)):
            if int(T[i][j]) > int(maxBin[j]):
                maxBin = T[i]
                break
    print(maxBin)
#zadanie3()


# Zadanie 5
def AddBin(bin1, bin2):
    wynik = ""
    suma = 0
    for i in range(len(bin1)):
        suma += (int(bin1[-1-i]) + int(bin1[-1-i]))
        wynik = str(suma % 2) + wynik
        suma = suma // 2
    if suma > 0:
        wynik = str(suma) + wynik
    return wynik
#print(AddBin("10101", "111"))

def MultBin(bin1, bin2):
    wynik = ""
    for i in range(len(bin2)):
        if bin2[-1-i] == 1:
            wynik = AddBin(wynik, bin1)
        bin1 = bin1 + "0"


    return wynik


print(MultBin("10101", "00111"))
