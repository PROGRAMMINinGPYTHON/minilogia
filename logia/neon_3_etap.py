

def kolumny_na_wiersze(lista):
    kolumna= []
    for i in range(len(lista[0])):
        wiersz = [lista[j][i] for j in range(len(lista[0]))]
        kolumna.append(wiersz)
    return  kolumna


print(kolumny_na_wiersze([[2,10,3],[9,4,3],[1,2,3]]))