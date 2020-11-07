
def ilerazy(n,lista):
    ilen = 0
    suma = 0
    for i in range(len(lista)):
        if i%2 == 0:
            if suma<n and suma+lista[i]>=n:
                ilen += 1
            suma += lista[i]
        else:
            if suma>n and suma-lista[i]<=n:
                ilen +=1
            suma -= lista[i]
    return ilen

print(ilerazy(4,[5,3,5,3,2,1]))