tablica = [9, 8, 7, 5]

#
# def zamiana(a, b, tab):
#     tmp = tab[a]
#     tab[a] = tab[b]
#     tab[b] = tmp
#
#
# def wstw_do_pos(poz, tab):
#     while poz > 0 and tab[poz] < tab[poz - 1]:
#         zamiana(poz, poz - 1, tab)
#         poz = poz - 1
#
#
# def sortowanie(tab):
#     for i in range(0, len(tab)):
#         wstw_do_pos(i, tab)
#

def sortowanie_bombelki(tab):
    for j in range(len(tab)-1):
        for i in range(len(tab)-1):
            if tab[i] > tab[i + 1]:
                tmp = tab[i]
                tab[i] = tab[i + 1]
                tab[i + 1] = tmp
        print(tab)


print(tablica)
sortowanie_bombelki(tablica)
print(tablica)
