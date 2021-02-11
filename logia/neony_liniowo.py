

def neon(lista):
    naj = 0
    pom = lista[0]
    for x in lista[1:]:
        pom = pom+2
        naj = max(naj,pom +x)
        pom = max(pom,x)
    return naj

print(neon([1,10,1]))

