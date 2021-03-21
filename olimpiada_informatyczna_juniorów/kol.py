def pociag():
    wyniki = []
    q = input()
    q = q.split()
    for m in range(3):
        q[m] = int(q[m])
    liczba_miast = q[0]
    ile_miejsc = q[1]
    liczba_zgloszen = q[2]
    tab = []
    for w in range(liczba_miast + 1):
        tab.append(0)
    for i in range(liczba_zgloszen):
        a = input()
        a = a.split()
        for j in range(3):
            a[j] = int(a[j])

        czy_ok = True

        # sprawdzenie czy mozemy przyjac rezerwacje

        for k in range(a[0], a[1]):
            if tab[k] + a[2] > ile_miejsc:
                czy_ok = False
                break

        if czy_ok:
            # print("T")
            wyniki.append("T")
            # TODO przyjmij zgloszenie
            for c in range(a[0], a[1]):
                tab[c] += a[2]
        else:
            # print("N")
            wyniki.append("N")

    print('\n'.join(wyniki))
    print()


pociag()
