def oij(tab):
    jedna_z_liter = ['o', 'i', 'j']
    ile = 0
    j = 0
    for i in range(len(tab)):
        if tab[i] == jedna_z_liter[j]:
            j += 1
            if j == 3:
                ile += 1
                j = 0
    return ile if (ile > 0) else "NIE"

print(oij(list(input())))

oczekiwany_wynik = {
    "oijoij": 2,
    "oaiobjibojicj": 2,
    "jio": "NIE",
    "oijoijoijoij": 4,
    "oijo": 1,
    "aboijo": 1,
    "aboijoa": 1,
    "aboabiabjaboabijoi": 2,
    "abc": "NIE",
    "koligacjeomijaj": 2
}


def testowanie():
    for key in oczekiwany_wynik:
        print("testuje dla", key, "otrzymany wynik", oij(key), "oczekiwany wynik", oczekiwany_wynik[key])
        assert oij(key) == oczekiwany_wynik[key]

# testowanie()
