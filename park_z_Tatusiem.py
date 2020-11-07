def wczyt_tabl():
    a = int(input())
    tab = []
    for i in range(a):
        b = input()
        tab.append(b)
    return tab


def najw_na_zach(tab, idx):
    return max_szukaj(tab,0,idx+1)

def najw_na_wsh(tab, idx):
    return max_szukaj(tab,idx,len(tab))

def max_szukaj(tab,od_kad,do_kad):
    max = tab[od_kad]
    for k in range(od_kad,do_kad):
        if tab[k]>max:
            max = tab[k]
    return max


def park():
    tab = wczyt_tabl()
    for i in range(len(tab)):
        najw_zach = najw_na_zach(tab, i)
        najw_wsh = najw_na_wsh(tab, i)
        print(najw_na_zach(tab,i),najw_na_wsh(tab,i))

park()
