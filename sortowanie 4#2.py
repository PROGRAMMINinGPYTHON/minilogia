tab = [8, 2, 5, 2, 1]


def największa_wartość(tablica):
    największa = tablica[0]
    for i in range(len(tab)):
        if tab[i] > największa:
            największa = tab[i]
    return największa

def idx_największej_wartości(tablica):
    idx_najwiekszej = 0
    for i in range(len(tab)):
        if tab[i] > tab[idx_najwiekszej]:
            idx_najwiekszej = i
    return idx_najwiekszej

def index_największej_wartości(tablica):
    index = 0
    max = największa_wartość(tablica)
    for j in range(len(tab)):
        if tablica[j] == max:
            index = j
            return index
    print(index)


print(największa_wartość(tab))
