tab = ["Sitek","Zagorska","Ławniczak","Dubasiewicz","Krakus","Putkiewicz","Chomicka","Bogdan","Stolowski","Wysocki","Wisnewska","Sulich","Dowgiert","Ortynski","Olszewska","Kozak"]



def sortowanie(tab):
    for j in range(2):
        for i in range(len(tab) - 1):
            if tab[i] > tab[i + 1]:
                zamiana(i, tab)


def zamiana(i, tab):
    tmp = tab[i]
    tab[i] = tab[i + 1]
    tab[i + 1] = tmp
    print(tab)


sortowanie(tab)
print(tab)
print(len(tab))
