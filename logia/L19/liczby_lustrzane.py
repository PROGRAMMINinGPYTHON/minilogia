def lustro(liczba, ile_prob):
    for i in range(ile_prob):
        if jest_palind(suma(liczba)):
            return suma(liczba)
        else:
            liczba = liczba+odwrocenie(liczba)
    return - 1

def lustro2(liczba, ile_prob):
    if (ile_prob == 0): return -1
    if jest_palind(suma(liczba)):
        return suma(liczba)
    else:
        return lustro(liczba+odwrocenie(liczba), ile_prob-1)

def odwrocenie(liczba):
    liczba = str(liczba)
    liczba = list(liczba)
    od_tylu = []
    for i in range(len(liczba)):
        od_tylu.append(liczba[-i - 1])
    x = liczba[0]
    y = od_tylu[0]
    for i in range(len(liczba) - 1):
        y = y + od_tylu[i + 1]
    y = int(y)
    return y


def suma(liczba):
    suma = liczba + odwrocenie(liczba)
    return suma


def jest_palind(suma):
    suma = str(suma)
    suma = list(suma)
    for j in range(len(suma)):
        if suma[j] == suma[-j-1]:
            pass
        else:
            return False
    return True

print(lustro(91 ,1))
print(lustro2(91 ,1))
print(lustro(91 ,2))
print(lustro2(91 ,2))
print(lustro(125 ,3))
print(lustro2(125 ,3))
print(lustro(910 ,1))
print(lustro2(910 ,1))
print(lustro(910 ,2))
print(lustro2(910 ,2))
print(lustro(9101 ,2))
print(lustro2(9101 ,2))