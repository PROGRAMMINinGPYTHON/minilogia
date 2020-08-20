tab = [1,1,9,4,3,2,6,4,8,1,7,0,5,3,4,55,1111111111]

def sortuj(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i]<tab[j]:
                a = tab[i]
                tab[i] = tab[j]
                tab[j]= a
                print(tab)










