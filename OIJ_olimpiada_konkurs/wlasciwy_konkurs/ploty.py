global wyjscie
wyjscie = []
def przecina(plot, inny):
    return (plot[1] > inny[0] and plot[0] < inny[0] and plot[1] < inny[1]) or (inny[1] > plot[0] and inny[0] < plot[0] and inny[1] < plot[1])


def wypisz(p):
    wyjscie.append(p)

def znajdz(ploty):
    przeciecia = set()
    for plot in ploty:
        for inny in ploty:
            if (plot[1] > inny[0] and plot[0] < inny[0] and plot[1] < inny[1]) or (inny[1] > plot[0] and inny[0] < plot[0] and inny[1] < plot[1]):
                przeciecia.add(plot)
                przeciecia.add(inny)

    if (len(przeciecia)) == 2:
        wypisz(next(iter(przeciecia)))
    else:
        sek = iter(przeciecia)
        p1 = next(sek)
        p2 = next(sek)
        p3 = next(sek)
        if przecina(p1, p2) and przecina(p1, p3):
            wypisz(p1)
        elif przecina(p2, p1) and przecina(p2, p3):
            wypisz(p2)
        else:
            wypisz(p3)


def ploty():
    Z = int(input())
    for i in range(Z):
        N = int(input())
        ploty = []
        for j in range(N - 2):
            plot = [int(x) for x in input().split()]
            if (plot[0] > plot[1]):
                ploty.append((plot[1], plot[0]))
            else:
                ploty.append((plot[0], plot[1]))

        znajdz(ploty)



ploty()
for p in wyjscie:
    print(p[0], p[1])

