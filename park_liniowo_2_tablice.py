def wczyt_tabl():
    a = int(input())
    tab = []
    for i in range(a):
        b = input()
        tab.append(b)
    return tab


def przygotuj_max_lewo(tab):
    max_tab = []
    max_elem = tab[0]
    for i in range(len(tab)):
        if tab[i] > max_elem:
            max_elem = tab[i]
        max_tab.append(max_elem)
    return max_tab


def przygotuj_max_prawo(tab):
    max_tab = []
    max_elem = tab[-1]
    for i in range(-1, -len(tab)-1, -1):
        if tab[i] > max_elem:
            max_elem = tab[i]
        max_tab.insert(0,max_elem)
    return max_tab


def park():
    tab = wczyt_tabl()
    max_lewo_tab = przygotuj_max_lewo(tab)
    max_prawo_tab = przygotuj_max_prawo(tab)
    print(max_lewo_tab)
    print(max_prawo_tab)
    for i in range(len(tab)):
        print(max_lewo_tab[i], max_prawo_tab[i])


park()
