import math



a = int(input())
b = input()

def xxxxxx (a):
    ile = 0
    for i in range(1,a+1):
        ile += math.floor(i/2)
    print( ile)

def psikus(droga):
    lcz = 0
    for j in range(0,len(droga)):
        pom = 0

        for i in range(j,len(droga)):
            pom = pom+droga[i]
            if pom %2 == 0:
                lcz += 1
    return lcz


for i in range(a):
    if b[i] % == 1:
        psikus(b)
        break
    else:
        pass
xxxxxx(a)

# test = {1:0,2:1,3:2,4:4,5:6,6:9}
# def testy():
#     for i in range(1,6):
#         print(xxxxxx(i))
#         assert xxxxxx(i) == test[i]
#
# testy()
#
