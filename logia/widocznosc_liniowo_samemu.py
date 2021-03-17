def widocznosc(wejscie):
    talerze = []
    for i in range(len(wejscie)):
        while len(talerze) > 0 and talerze[-1][0] <= wejscie[i]:
            talerze.pop()

        if len(talerze) == 0:
            print(-1)
        else:
            print(talerze[-1][1] + 1)
        talerze.append((wejscie[i], i))

widocznosc([8, 4, 2, 5, 7, 8])
