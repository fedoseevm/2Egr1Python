# KONWERSJA BIN -> DEC
def ConvertDecToBin(numberDec):
    output = ""
    while numberDec > 0:
        output = str(numberDec % 2) + output
        numberDec = numberDec // 2
    return int(output)


def ConvertDecToBinReku(numberDec):
    if numberDec == 0: return ""
    return ConvertDecToBinReku(numberDec // 2) + str(numberDec % 2)


def ConvertDecToBinRekuWithSteps(numberDec):
    if numberDec == 0: return
    ConvertDecToBinRekuWithSteps(numberDec // 2)
    print(numberDec % 2, end = "")
    


print("Podaj liczbe (system dziesiety): ", end="")
liczbaDec = int(input())
print("Iteracyjnie: ", end="")
print(ConvertDecToBin(liczbaDec))
print("\n")

print("Rekurecyjnie: ", end="")
print(ConvertDecToBinReku(liczbaDec))
print("\n")

print("Rekurecyjnie z krokami : ")
print(ConvertDecToBinRekuWithSteps(liczbaDec))
print("\n")






# KONWERSJA BIN -> DEC
def ConvertBinToDec(numberBin):
    inputNumber = str(numberBin)
    output = 0
    for i in range(len(inputNumber)):
        output += (2 ** i) * int(inputNumber[-1 - i])
    return output

def ConvertBinToDec2(numberBin):
    inputNumber = str(numberBin)
    output = 0
    potega = 1
    for i in range(len(inputNumber)):
        output += potega * int(inputNumber[-1 - i])
        potega *= 2
    return output

def ConvertBinToDecHornera(numberBin):
    inputNumber = str(numberBin)
    output = 0
    for i in range(len(inputNumber)):
        output = output * 2 + int(inputNumber[i])
    return output

print("Podaj liczbe (system binarny): ", end="")
liczbaBin = int(input())
print("Wersja 1: ", end="")
print(ConvertBinToDec(liczbaBin))
print("\n")

print("Wersja 2 (z osobna zmienna potegi): ", end="")
print(ConvertBinToDec2(liczbaBin))
print("\n")

print("Wersja 3 (Hornera): ", end="")
print(ConvertBinToDecHornera(liczbaBin))
print("\n")