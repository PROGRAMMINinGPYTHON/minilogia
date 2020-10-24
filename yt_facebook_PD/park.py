a =int( input())
tab = []
for i in range(a):
    b = input()
    tab.append(b)

def najw_na_zach(punkt):
    najw_na_y = -1
    for i in range(0,punkt):
        if int(tab[i])>int(najw_na_y):
            najw_na_y = tab[i]
    return najw_na_y

def najw_na_wsh(punkt):
    najw_na_x = -1
    for j in range(punkt,len(tab)):
        if int(tab[j])>int(najw_na_x):
            najw_na_x = tab[j]
    return najw_na_x

for y in range(len(tab)):
    print(najw_na_zach(y))
    print(najw_na_wsh(y))



