

def calosc(n, a):
    for j in range(n - 1):
        suma = 0
        while a > 0:
            suma += a % 10
            a //= 10
        a = suma * 2
    return a


def dodanie_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma


def wczytanie():
    a = input()
    a = a.split()
    print(a)
    return int(a[0]), int(a[1])


def wieksze(n, a):
    tab = [10, 2, 4, 8, 16, 14]
    if n == 1:
        return (1)
    else:
        return (tab[n % 6 - 1])


def wszystko(n, a):
    # return calosc(n, a)
    if a == 1:
        return wieksze(n, a)
    else:
        return calosc(n, a)

a = input()
a = a.split()
a[0] = int(a[0])
a[1] = int(a[1])
print(calosc(a[0], a[1]))
