tab = [7,4,2,6,2,1,5,7,3]

def sortowanie3(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            print(tab)
            if tab[j]>tab[j+1]:
                a = tab[j]
                tab[j]  = tab[j+1]
                tab[j+1] = a
            else:
                continue

sortowanie3(tab)
print (tab)