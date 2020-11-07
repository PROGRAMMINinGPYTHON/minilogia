def wczyt_tabl():
    a = int(input())
    tab = []
    for i in range(a):
        b = input()
        tab.append(b)
    return tab
def przygotuj_max_prawo(tab):
    max_tab = []
    max_elem = tab[-1]
    for i in range(-1, -len(tab) - 1, -1):
        if tab[i] > max_elem:
            max_elem = tab[i]
        max_tab.insert(0, max_elem)
    return max_tab
def park():
    tab = wczyt_tabl()
    max_elem = tab[0]
    max_prawo_tab = przygotuj_max_prawo(tab)
    for i in range(len(tab)):
        if (tab[i] > max_elem): max_elem = tab[i]
        print(max_elem, max_prawo_tab[i])
park()
