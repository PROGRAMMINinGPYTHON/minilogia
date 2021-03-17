def glowna_funkcja():
    a = input()
    wczytanie = input().split()
    wczytanie = list(wczytanie)
    for i in range(len(wczytanie)):
        wczytanie[i] = int(wczytanie[i])
    tablica_sum = []
    suma_wszystkich = 0
    for j in range(len(wczytanie)):
        suma_wszystkich += wczytanie[j]
        tablica_sum.append(suma_wszystkich)
    a = a.split()
    tablica_sum.insert(0,0)
    zwrot = []
    for q in range(int(a[1])):
        x = input()
        x = x.split()
        zwrot.append(tablica_sum[int(x[1])]-tablica_sum[int(x[0])-1])
    for m in range(len(zwrot)):
        print(zwrot[m])




glowna_funkcja()