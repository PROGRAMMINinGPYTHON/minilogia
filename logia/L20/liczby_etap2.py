from turtle import *


def suma_cyfr_rowna_iloczynowi_cyfr(liczba):
    suma = 0
    iloczyn = 1
    for litera in str(liczba):
        suma += int(litera)
        iloczyn *= int(litera)

    return suma == iloczyn


def ile(lista):
    wynik = 0

    for liczba in lista:
        if suma_cyfr_rowna_iloczynowi_cyfr(liczba):
            wynik += 1

    return wynik


print(ile([7, 13, 1122, 111, 52, 52111]))
print(ile([11, 1000, 123]))
print(ile([321, 152, 2141, 4211]))
