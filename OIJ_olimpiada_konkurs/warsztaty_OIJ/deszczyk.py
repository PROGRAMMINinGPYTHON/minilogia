
print("a")

def deszczyk():
    a = input()
    a = a.split()
    for i in range(len(a)):
        a[i] = int(a[i])
    liczba_dni = a[0]
    liczba_miast = a[1]
    liczba_zapytan = a[2]
    opisy_dni = []
    for j in range(liczba_dni):
        opisy_dni.append(input())
    print(opisy_dni)
    for k in range(len(opisy_dni)):
        opisy_dni[k] = opisy_dni[k].split()
        for l in range(3):
            opisy_dni[k][l] = int(opisy_dni[k][l])
    print(opisy_dni)
    tablica_opadow = []
    for n in range(liczba_miast+1):
        tablica_opadow.append(0)
    print(tablica_opadow)
    for m in range(len(opisy_dni)):
        tablica_opadow[opisy_dni[m][0]]+= opisy_dni[m][2]
        print(tablica_opadow)
        # print(tablica_opadow[opisy_dni[m][1]] -= opisy_dni[m][1])


deszczyk()


