def tablica():
    tab = []
    a = int(input())
    for i in range(a):
        i = int(input())
        tab.append(i)
    return tab


def maxWsch(tab, poz_start):
    najW = tab[poz_start]
    for i in range(poz_start,len(tab)):
        if najW<tab[i]:
            najW = tab[i]
    return najW


def maxZach(tab, poz_start):
    najZ = tab[poz_start]
    for i in range(poz_start,0,-1):
        if najZ<tab[i]:
            najZ = tab[i]
    return najZ


def park():
    tab = tablica()
    for i in range(len(tab)):
        zach = maxZach(tab, i)
        wsch = maxWsch(tab, i)
        print(zach, ' ', wsch)

#największa_na_zach(3)
park()

