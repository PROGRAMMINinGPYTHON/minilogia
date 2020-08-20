N = int(input())
L = [int(l) for l in input().split()]

idx = 0

licznik = 0
while (idx < len(L)-1):
    while (idx < len(L)-1 and L[idx + 1] >= L[idx]):
        idx+=1

    licznik+=1

    if (idx < len(L)-1):
        while (idx < len(L) - 1 and L[idx + 1] <= L[idx]) :
            idx += 1
        licznik+=1

if (len(L) == 1):
    licznik = 1
print(licznik)
