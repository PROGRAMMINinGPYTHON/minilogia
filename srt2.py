tablica = [2,1,100,91,1,9,4]

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

# def sortowanie_bombelki(tab):
#     for j in range(len(tab)-1):
#         for i in range(len(tab)-1):
#             if tab[i] > tab[i + 1]:
#                 tmp = tab[i]
#                 tab[i] = tab[i + 1]
#                 tab[i + 1] = tmp
#         print(tab)

def najw(tab,i):
    najW = 0
    for j in range(len(tab)-i):
        if tab[j]>tab[najW]:
            najW = j
    return najW

def sortowanie_wyb(tab):
    for i in range(len(tab)):
        tmp = tab[-1-i]
        tab[-1-i] = tab[najw(tab,i)]
        tab[najw(tab,i)]= tmp

print(tablica)
sortowanie_wyb(tablica)
print(tablica)

