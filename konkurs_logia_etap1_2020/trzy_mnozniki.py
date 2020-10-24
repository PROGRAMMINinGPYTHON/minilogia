# a = input()
# M = 3

tab= [9,8,7,4,3,1,8]
poczatek = 0
koniec = 7
suma = 0
iloczyn = 1
for i in range(poczatek,koniec):
    suma = suma+tab[i]
    iloczyn = iloczyn * tab[i]


print(suma)
print(iloczyn)
