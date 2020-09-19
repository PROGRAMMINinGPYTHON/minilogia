def ile(lista):
    wynik_koncowy = 0
    for i in range(len(lista)):
        #    mnożenie(lista, i)
        #    dodawanie(lista, i)
        if dodawanie(lista[i]) == mnożenie(lista[i]):
            wynik_koncowy = wynik_koncowy + 1
    return wynik_koncowy


def mnożenie(liczba):
    wynik_mnoż = 1
    for x in str(liczba):
        wynik_mnoż = wynik_mnoż * int(x)
    return wynik_mnoż


def dodawanie(liczba):
    wynik_dodaw = 0
    for x in str(liczba):
        wynik_dodaw = wynik_dodaw + int(x)
    return wynik_dodaw


print(ile([7, 13, 1122, 111, 52, 52111]))
print(ile([11, 1000, 123]))
print(ile([321, 152, 2141, 4211]))
