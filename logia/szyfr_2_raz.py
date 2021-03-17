def deszyfr(lista):
    zwrocenie = []
    for i in range(len(lista)):
        zwrocenie.append(deszyfr_jednego_ciagu_liczb(lista[i]))
    print(zwrocenie)


def deszyfr_jednego_ciagu_liczb(ciag_liczb):
    zwrot = ""
    for i in range(0, len(str(ciag_liczb)), 2):
        liczba = str(ciag_liczb)[i] + str(ciag_liczb)[i + 1]
        if int(liczba) > 33:
            zwrot = zwrot + deszyfr_jeden_liczby_do_40(liczba)
        else:
            zwrot = zwrot + deszyfr_jeden_liczby_do_20(liczba)
    return zwrot


def deszyfr_jeden_liczby_do_20(liczba):
    liczba = int(liczba)
    return chr(97 - 21 + liczba)


def deszyfr_jeden_liczby_do_40(liczba):
    liczba = int(liczba)
    return chr(110 - 41 + liczba)


deszyfr([332131425021, 4321412925413121])
deszyfr([31452122])
