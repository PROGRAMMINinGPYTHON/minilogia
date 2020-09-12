tablica = [0,2,6,1,9]

def największa(tab):
    sraka = tab[0]
    for i in range(len(tab)):
        if tab[i]>sraka:
            sraka = tab[i]
    return sraka

    # tutaj chce policzyć.....
    idx = 0
    for i in range(len(tab)):
        if tab[i] == największa(tab):
            return i


def sortowanie(tab):
    idx = 0
    for i in range(len(tab)):
        if tab[i]== największa(tab)
            return i

    for i in range(len(tab)):
        tmp = tab[-1-i]
        tab[-1-i] = tab[idx]
        tab[idx] = tmp

sortowanie(tablica)