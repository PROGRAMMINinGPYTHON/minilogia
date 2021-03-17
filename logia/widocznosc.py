def widocznosc(wejscie):
    wyjscie = []
    for i in range(len(wejscie)):
        znalazl = False
        for j in range(i, -1, -1):
            if wejscie[j] > wejscie[i]:
                print(j + 1)
                znalazl = True
                break
        if znalazl == False:
            print("-1")
        znalazl = False


widocznosc([8, 4, 2, 5, 7, 8])
