tab = [4, 3]


def sortowanie(tablica):
    for i in range(len(tablica)):
        wstaw_element(tablica, i)


def wstaw_element(tablica, i):
    while tablica[i] < tablica[i - 1] and i > 0:
        zamiana(tablica,tablica[i], tablica[i - 1])
        i = i - 1


def zamiana(tablica,x, y):
    tmp = tablica[x]
    tablica[x] = tablica[y]
    tablica[y] = tmp



sortowanie(tab)
print(tab)


x = 5
y = 7
zamiana ()