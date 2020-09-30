tablica = [5, 2, 1, 4]


def sortowanie(tab):
    for j in range(2):
        for i in range(len(tab) - 1):
            if tab[i] > tab[i + 1]:
                zamiana(i, tab)
                print(tab)


def zamiana(i, tab):
    tmp = tab[i]
    tab[i] = tab[i + 1]
    tab[i + 1] = tmp


sortowanie(tablica)
