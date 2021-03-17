
def klucz(tablica):
    return (tablica[1],tablica[0])


def roztopy():
    tablica_wczyt = []
    a = input()
    a = int(a)
    tablica_wczyt.append((0,0))
    for i in range(a):
        x = input()
        x = x.split()
        tablica_wczyt.append(("apoczatek",int(x[0])))
        tablica_wczyt.append(("bkoniec",int(x[1])))
    sorted(tablica_wczyt,key=klucz)
    print("_________________________")
    print(tablica_wczyt)
    b = 0
    lcz = 0
    najw = lcz
    while b < len(tablica_wczyt)-1:
        b += 1
        if tablica_wczyt[b][1] == "apoczatek":
            lcz += 1
        else:
            lcz -= 1
        if lcz >najw:
            najw += 1
        print(najw)
roztopy()


