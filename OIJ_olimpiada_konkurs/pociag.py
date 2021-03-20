#
# def pociag():
#     liczba_miast = int(input())
#     ile_miejsc = int(input())
#     n = int(input())
#     tab = []
#     for w in range(liczba_miast+1):
#         tab.append(0)
#     for i in range(n):
#         a = input()
#         a = a.split()
#         for j in range(3):
#             a[j] = int(a[j])
#         for k in range(a[0],a[1]):
#             tab[k] += a[2]
#             if tab[k] > ile_miejsc:
#                 print("N")
#                 break
#             else:
#                 if k == a[1]-1 and tab[k]+a[2] <= ile_miejsc:
#                     print("T")
#                     break
# #
# # pociag()
# #
# #
# # pociag()

def mozna_przyjac_rezerwacje(od, do, ile_rezerwacji, tab, liczba_miejsc_w_pociagu):
    return True


def pociag():
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
            if tab[k] > ile_miejsc:
                czy_ok = False
                break

        if czy_ok:
            print("T")
            # TODO przyjmij zgloszenie
            for c in range(a[0], a[1]):
                tab[c] += a[2]
        else:
            print("N")


pociag()
