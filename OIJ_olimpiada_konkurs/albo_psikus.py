
def psikus(droga):
    lcz = 0
    for j in range(0,len(droga)):
        pom = 0

        for i in range(j,len(droga)):
            pom = pom+droga[i]
            if pom %2 == 0:
                lcz += 1
    return lcz

def wczytanie():
    a = int(input())
    b = input()
    b = b.split()
    for i in range(a):
        b[i] = int(b[i])
    return b
print(psikus(wczytanie()))


