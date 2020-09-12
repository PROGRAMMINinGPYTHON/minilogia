# a = 5
# b = 3
# c = 6
# d = 5
#
# def aaa (a,b,c,d):
#     a = a+2
#     print("a funkcja")
#     print(a)
#     b = b*2
#     print(b)
#     c = c
#     print(c)
#
# print(a)
# print(b)
# print(c)
# aaa(a,b,c,d)
# print(a)
# print(b)
# print(c)
#
# tab = [0,3,5,2,1]
#
# def sssssssss(tab2):
#     tab2.append(45)
#
#     print(tab2)
#     tab2 = [4,4,5,5]
#     print (tab2)
#
#
# sssssssss(tab)
# #tab.remove(3)
# print("===============")
# print(tab)

#
# a = 43
# a2 = a
# b = 35
# b2 = b
# c = a+b
# d = c*a
#
# def funkcja_zmienna (aa, bb, c, d):
#
#     print("w funkcji")
#     aa = aa + bb
#     print("a = ")
#     print(aa)
#     print("poza funkcją")
#     print(a2)
#     bb = 83
#     print(bb, b2)
#
# funkcja_zmienna(a,b,c,d)
#
# print("--------------------------------")
# tablica = [0, 4, 2, 1, 6, "kot"]
# tablica2 = tablica
# print(tablica)
# def funkcja_tablica(tab):
#     tab2 = [5,"pies"]
#     tab.append("345")
#     tab = tab2
#     print(tab)
# funkcja_tablica(tablica)
# print("poza funkcją")
# print(tablica)
#
# print("-------------------")
#
#
#
tab = [0,3]
tab2 = tab

print(tab,tab2)
print("dddd")
def tablica(tablica):
    print(tab)
    print(tab2)
    tab.append(4)
    print(tab)
    tab2.remove(3)
    print(tab,tab2)

tablica(tab)
print(tab,tab2)