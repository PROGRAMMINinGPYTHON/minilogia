def dupadupadupadupadupa(tab):
    for i in range(len(tab)):
        for j in range(i,len(tab)):
            if tab[i]>tab[j]:
                tmp = tab[i]
                tab[i] = tab[j]
                tab[j] = tmp
            print(tab)
sraka = [3,2,1,4]
dupadupadupadupadupa(sraka)