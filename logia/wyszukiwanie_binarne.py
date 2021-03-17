import math


def szukanie(liczba, tablica):
    if liczba < tablica[0]:
        print("error")
        return -1
    if liczba > tablica[-1]:
        print("error")
        return -1
    if liczba == 0:
        print(0)
        return 0
    szukana = liczba
    tab = tablica
    d = len(tab)
    idx = math.ceil(d / 2)
    zakres = [0, len(tab) - 1]
    while True:
        if szukana > tab[idx]:
            zakres[0] = idx
            idx = math.ceil((zakres[0] + zakres[1]) / 2)
        else:
            zakres[1] = idx
            idx = math.ceil((zakres[0] + zakres[1]) / 2)
        if tab[idx] == szukana:
            print("sukces")
            print(idx)
            return idx
        print(zakres)
        # if zakres[1] - zakres[0] == 1:
        #     print("duuuuuuupa")
        #     return -1
        #     break

# szukanie(szukana, tab)
# szukanie(4,[1,2,3,4])
# szukanie(4, [-1,1,2,3,5,6,7,8,8,9,9])
# szukanie(-1, [-1, 3, 8,9,10])
# print("ost ", szukanie(-1, [0,1,2,3,4,5,6,7,8,8,9,9]))
