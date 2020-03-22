##tab =["a","b","e","c","ddsdfsdasfasf"]

def sortowanie(tab):
    print("input ", tab)
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i]<tab[j]:
                tmp = tab[i]
                tab[i] = tab[j]
                tab[j] = tmp
    print("sortd ", tab)    
#    print(tab*2)
