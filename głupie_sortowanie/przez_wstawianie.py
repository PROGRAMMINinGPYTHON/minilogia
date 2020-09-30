tablica = [9, 8, 7, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]


def zamiana(a, b, tab):
    tmp = tab[a]
    tab[a] = tab[b]
    tab[b] = tmp


def wstaw_do_posortowanej(poz, tab):
    while poz > 0 and tab[poz] < tab[poz - 1]:
        zamiana(poz, poz - 1, tab)
        poz = poz - 1


def sortuj(tab):
    for i in range(0, len(tab)):
        wstaw_do_posortowanej(i, tab)


sortuj(tablica)
print(tablica)
