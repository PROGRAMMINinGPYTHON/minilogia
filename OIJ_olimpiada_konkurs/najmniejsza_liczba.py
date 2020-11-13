def najmniejsza(linia):
    tab = linia.split()
    for k in range(0, 3):
        tab[k] = int(tab[k])
    tab.sort()
    x = []
    l = []
    for i in range(3):
        if tab[i] > 0:
            l.append(tab[i])
        else:
            if tab[0] == 0 and tab[i] == 0:
                x.append(tab[i])
            else:
                l.append(tab[i])
    for y in range(len(x)):
        l.insert(1, x[y], )
    return l


def wypisz(l):
    for o in range(len(l)):
        print(l[o], end="")


wypisz(najmniejsza(input()))

dane = {
    "1 3 2": [1, 2, 3],
    "0 1 2": [1, 0, 2],
    "0 1 3": [1, 0, 3],
    "0 0 9": [9, 0, 0],
    "1 0 0": [1, 0 ,0],
    "0 9 0": [9, 0, 0]
}


def test():
    for klucz in dane:
        print ("testuje dla ", klucz)
        assert najmniejsza(klucz) == dane[klucz]


#test()
