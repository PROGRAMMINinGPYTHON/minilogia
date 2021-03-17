import math


def wyszukiwanie(tab, szukana):
    p = len(tab)-1
    l = 0
    while p - 1 > l:
        srodek = math.ceil((p + l) / 2)
        if tab[srodek]  == szukana:return srodek
        if tab[srodek]>szukana:
            if p == srodek:
                p = srodek-1
            else:
                p = srodek
        else:
            if l == srodek:
                l = srodek+1
            else:
                l = srodek
        if tab[l] == szukana:
            return l
        else:
            return -1
print(wyszukiwanie([0,1,2,3],2))