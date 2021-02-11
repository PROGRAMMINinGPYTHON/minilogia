
a = input()
b = input()

b = b.split()
tab_mocy = b

for i in range(len(tab_mocy)):
    tab_mocy[i] = int(tab_mocy[i])

tab_mocy.sort()


for i in range(10):
    print(tab_mocy[-1-i],end=" ")