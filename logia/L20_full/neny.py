def neony (a):
    naj = 0
    pom = a[0]
    for i in a[1:]:
        pom += 2
        pom = max(pom,i)
        naj = max(naj,pom+i)
    return naj

def neony (a):
    naj = 0
    pom = a[0]
    for x in  a[1:]:
        pom += 2
        naj = max(naj,pom+i)
        pom = max(pom,i)