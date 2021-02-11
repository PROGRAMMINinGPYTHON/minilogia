

def ile(lista):
    lcz = 0
    for i in range(len(lista)):
        lista[i] = str(lista[i])
        lista[i] = list(lista[i])
        suma = int(lista[i][0])
        mnoz = int(lista[i][0])
        for j in range(1,len(lista[i])):
            suma = suma+int(lista[i][j])
        for k in range(1,len(lista[i])):
            mnoz = mnoz * int(lista[i][k])
        if mnoz == suma:
            lcz += 1
    return lcz

ile([7, 13, 1122, 111, 52, 52111])
ile([11, 1000, 123])
ile([321, 152, 2141, 4211])
