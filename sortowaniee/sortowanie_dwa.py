def sortowanie(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i] < tab[j]:
                tmp = tab[i]
                tab[i] = tab[j]
                tab[j] = tmp
            print(tab)
            # else:
            #     tmp = tab[j]
            #     tab[j]= tab[i]
            #     tab[i] = tmp

sss = [2,1,4,3]
sortowanie(sss)



