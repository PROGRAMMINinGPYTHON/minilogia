def ile(n):
    v = 2
    okr = 1
    par = 3

    bok = 0
    while True:

        for i in range(1, 7):
            bok += 1
            if okr % 2 == 0 and i == 1:
                npar = -10
            else:
                npar = -1

            if bok % 2 == 1:
                v += npar
            else:
                v += par

            if bok == n:
                return v
        okr += 1


#print(ile(4))
print(ile(14))
print(ile(100))
