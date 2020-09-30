tab = [3,20,1,1,37,2,1,54564,6,34]

def sortowanie(tablica):
    for i in range(len(tab)):
        tmp = tablica[-i-1]
        tablica[-i-1] = tablica[index_największej_wartosci(tablica,i)]
        tablica[index_największej_wartosci(tablica,i)] = tmp
        print(tablica)

def index_największej_wartosci(tablica,i):
    index = 0
    for i in range(len(tablica)-i):
        if tab[i]>tab[index]:
            index = i
    print(index)
    return index

sortowanie(tab)