


def neon(tablica):
    naj = 0
    pomocnicza = tablica[0]
    for x in tablica[1:]:
        pomocnicza += 2
        naj = max(naj ,pomocnicza+x)
        pomocnicza = max(pomocnicza,x)
    return naj

print(neon([10,4,5,7,1,4,1]))