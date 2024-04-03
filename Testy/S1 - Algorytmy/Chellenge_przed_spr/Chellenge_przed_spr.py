# Zadanie 1
# Sprawdz czy wpisana przez usera liczba binarna jest parzysta

def zadanie1():
    print("podaj liczbe binarna: ", end = "")
    wejscie = input()
    if wejscie[-1] == "0":
        print("Liczba jest parzysta")
    else:
        print("Nieparzysta")

#zadanie1()

# Zadanie 2
# Okresl parzystosc sumy/roznicy/iloczynu dwoch wpisanych przez usera liczb binarnych
def zadanie2():
    print("Podaj perwsza liczbe binarna: ", end = "")
    liczba1 = input()
    print("Podaj perwsza liczbe binarna: ", end = "")
    liczba2 = input()

    #print("\nCo chcesz robic(+, -, *): ", end = "")    # Wersja z wyborem dzialania arytmetycznego (+, -, *)
    #znak = input()
    #if znak == "+" or znak == "-":
    #    if (liczba1[-1] == liczba2[-1]):
    #            print("Jest parzystosc!")
    #    else:
    #        print("Nie ma parzystosci :(")
    #elif znak == "*":
    #    if liczba1[-1] == "1" and liczba2[-1] == "1":
    #            print("Jest parzystosc!")
    #    else:
    #        print("Nie ma parzystosci :(")

    if (liczba1[-1] == liczba2[-1]):
        print("Suma jest parzysta.\nRoznica jest parzysta.")
    else:
        print("Suma nie jest parzysta.\nRoznica nie jest parzysta.")
    if liczba1[-1] == "1" and liczba2[-1] == "1":
        print("Iloczyn jest parzysty.")
    else:
        print("Iloczyn nie jest parzysty.")
#zadanie2()

# Zadanie 3
# 