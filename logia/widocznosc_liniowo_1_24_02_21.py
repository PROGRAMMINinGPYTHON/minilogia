def widocznosc(wejscie):
    stos = []
    for i in range(len(wejscie)):
        while len(stos) > 0 and stos[-1][0] <= wejscie[i]:
            stos.pop()

        if len(stos) == 0:
            print(-1)
        else:
            print(stos[-1][1] + 1)
        stos.append((wejscie[i], i))

widocznosc([8, 4, 2, 5, 7, 8])
