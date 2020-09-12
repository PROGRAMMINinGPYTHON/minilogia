#tab = [1,5,0,9,2]
# tablica = [3, 1]
tablica = [12,0,4,2,9,7,11]

def index(tablica, zakres):
    inx_najwiekszej = 0
    for i in range(len(tablica) - zakres):
        if tablica[i] > tablica[inx_najwiekszej]:
            inx_najwiekszej = i
    return inx_najwiekszej



def sortowanie(tablica):
    for i in range(len(tablica)):
        idx_max = index(tablica, i)
        zamien(tablica, idx_max,-1 - i )


def zamien(tablica, idx1, idx2):
    tmp = tablica[idx1]
    tablica[idx1] = tablica[idx2]
    tablica[idx2] = tmp


#        print(tablica)

print(tablica)
sortowanie(tablica)
print(tablica)
