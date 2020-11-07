tab = [9,8,7,0,1]
def sortowanie_bombelkowe(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            if tab[j]>tab[j+1]:
                tmp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = tmp



def sortowanie_wbiorcze(tab):
    max = 0
    for i in range(len(tab)):
        for j in range(len(tab)-i):
            if tab[j]>max :
                max = j
        tmp = tab[-i]
        tab[-i] = tab[max]
        tab[max] = tmp



def zamiana(a, b, tab):
    tmp = tab[a]
    tab[a] = tab[b]
    tab[b] = tmp
def wstaw_do_posortowanej(poz, tab):
    while poz > 0 and tab[poz] < tab[poz - 1]:
        zamiana(poz, poz - 1, tab)
        poz = poz - 1
def sortowanie_prez_wstw(tab):
    for i in range(0, len(tab)):
        wstaw_do_posortowanej(i, tab)



print(tab)
sortowanie_prez_wstw(tab)
print(tab)