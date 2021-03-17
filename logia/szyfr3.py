def deszyfr(lista):
    wynik = []

    for liczba in lista:
        wynik.append(deszyfr_liczba(liczba))

    print(wynik)
    return wynik


def deszyfr_znak(napis):

    liczba = int(napis)
    if liczba < 40:
        wynik = chr(ord('a') + liczba - 20 - 1)
    else:
        wynik = chr(ord('n') + liczba - 40 - 1)
    return wynik


def deszyfr_liczba(liczba):
    wynik = ""
    napis = str(liczba)

    for i in range(len(napis) // 2):
        wynik += deszyfr_znak("" + napis[2 * i] + napis[2 * i + 1])

    return wynik


deszyfr([31452122])
deszyfr([332131425021, 4321412925413121])
