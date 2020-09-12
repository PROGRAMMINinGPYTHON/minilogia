tab = [1, 2, 0, 8, 1, 6, 9]


def sortowanie(tablica):
    for x in range(len(tablica)):
        for i in range(len(tablica) - 1):
            if tablica[i] > tablica[i + 1]:
                zamiana(i, i + 1, tablica)
            print(tablica)


def zamiana(i, j, tablica):
    tmp = tablica[i]
    tablica[i] = tablica[j]
    tablica[j] = tmp


tab2 = [2, 0, 8, 1]
sortowanie(tab)
