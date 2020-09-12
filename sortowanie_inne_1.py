tablica1 = []
tablica2 = [1]
tablica3 = [1, 2]
tablica4 = [2, 1]
tablica5 = [2, 1, 3, 4, 5, 2, 1, 0, 9, -1]


# def sortowanie(tab):
#     pass
#
#
# def przepchniecie_tablicy(tab):
#     pass
#
#
# def index_najwiekszej_wartosci(tab):
#     pass


def sortowanie(tab):
    for i in range(len(tab)):
        tmp = tab[i]
        k = i - 1
        while (k >= 0 and tab[k] > tmp):
            tab[k + 1] = tab[k]
            k = k - 1
        tab[k+1] = tmp

sortowanie(tablica5)
print(tablica5)
