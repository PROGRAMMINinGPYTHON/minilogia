a = input()
a = list(a)
tab = [a[0], a[1], a[2]]
for i in range(len(a) - 3):
    if int(tab[0]) * int(tab[1]) * int(tab[2]) < int(a[i + 1]) * int(a[i + 2]) * int(a[i + 3]):
        tab.pop(0)
        tab.pop(0)
        tab.pop(0)
        tab.append(a[i + 1])
        tab.append(a[i + 2])
        tab.append(a[i + 3])

print(int(tab[0]) * int(tab[1]) * int(tab[2]))
