def wczyt():
    a = int(input())
    tab = []
    for i in range(a):
        b = input()
        tab.append(b)
    return tab

def max_p(tab):
    max_tab = []
    elem = tab[-1]
    for i in range(-1, -len(tab) - 1, -1):
        if tab[i] > elem:
            elem = tab[i]
        max_tab.insert(i, elem)
    return max_tab

def park():
    tab = wczyt()

    max_lewo = tab[0]
    max_prawo_tab = max_p(tab)
    for i in range(len(tab)):
        if tab[i] > max_lewo: max_lewo = tab[i]
        print(max_lewo, max_prawo_tab[i])

park()
