tab = [10,0, 6, 2, 9, 1]


def index(tab,d):
    idx = 0
    for i in range(len(tab)-d):
        if tab[i]>tab[idx]:
            idx = i
    return idx


def sortowanie(tab):
    for j in range(len(tab)):
        tmp = tab[-1-j]
        tab[-1-j] = tab[index(tab,j)]
        tab[index(tab,j)] = tmp
print(tab)
sortowanie(tab)
print(tab)
