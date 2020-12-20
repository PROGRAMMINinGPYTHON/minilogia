import time


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


# 10s
# def dodanie_cyfr(liczba):
#     liczba = str(liczba)
#     suma = 0
#     for znak in liczba:
#         suma = suma + int(znak)
#     return suma


# pierwsze, ponad 2s
# def dodanie_cyfr(liczba):
#     liczba = str(liczba)
#     liczba = list(liczba)
#     suma = 0
#     for i in range(len(liczba)):
#         suma = suma + int(liczba[i])
#     return suma


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


testy = [
    [6, 1, 14],
    [4, 9912, 6],
    [1, 1, 1],
    [2, 1, 2],
    [3, 1, 4],
    [4, 1, 8],
    [5, 1, 16],
    [6, 1, 14],
    [7, 1, 10],
    [8, 1, 2],
    [1, 10, 10],
    [1, 100, 100],
    [2, 10, 2],
    [2, 100, 2],
    [1000000, 9, 18],
    [1000000, 1, 8],
    [1000000, 2, 16],
    [10000000, 2, 16],

]


def testowanie():
    for test in testy:
        msg = "hello"
        start_time = time.time()
        # msg = " dla " + str(test[0]) + ", X: " + str(test[1]) + " otrzymany wynik" + str(
        #     wszystko(test[0], test[1])) + " oczekiwany wynik" + str(test[2])
        assert wszystko(test[0], test[1]) == test[2], f"blad {msg}"
        print("--- %s seconds ---" % (time.time() - start_time))


# testowanie()

inp = input().split()
#
# # start_time = time.time()
#
print(wszystko(int(inp[0]), int(inp[1])))
#
# print("--- %s seconds ---" % (time.time() - start_time))
