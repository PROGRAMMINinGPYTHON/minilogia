tab = [0,0,1,7,4,2,8,3,1]

def sortowanie(tab):
    for j in range(len(tab)):
        for i in range(len(tab)-1-j):
            if tab[i]>tab[i+1]:
                a = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = a
                print(tab)

sortowanie(tab)