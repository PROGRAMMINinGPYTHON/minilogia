
def sumuj(a,b):
    return a+b


class Osoba:
    imie="Franek"
    nazwisko="Kowalski"
    adres=None
    wiek = None
    __wyplata=4

    def __init__(self):
        print("wywolales konstruktor bezparametrowy")

    def __init__(self, wyplata, adres):
        print("wywolales konstruktor z parametrem wyplata: " + str(wyplata))
        self.__wyplata = wyplata
        self.adres = adres

    def ustawWyplata(self, wartosc):
        self.__wyplata = 3 * wartosc * 1.23

    def wypiszMnie(self, oczy):
        print(self.imie, self.nazwisko, "mam oczy: ", oczy)

    def opis(x, oczy):
        return "Wygladam wspaniale, " + x.__prywatnyOpis(oczy) + " zarabiam: " + str(x.__wyplata)

    def __prywatnyOpis(self, oczy):
        return self.imie + " ." + self.nazwisko + " mam oczy: " + oczy
    


karol = Osoba(4, "rosola")
karol.pustePole = "foo"
karol.imie = "Karol"
michal = Osoba(5, "Inidiry Ghandi")
michal.imie = "Michal"
o = michal

print(o.imie,o.nazwisko,o.wiek)
print(o)
print(o.nazwisko,o.wiek)

karol.wypiszMnie("zielone")
michal.wypiszMnie("niebieskie")

print (karol.opis("czerwone"))
#michal.ustawWyplata(10)
print (michal.opis("czerwone"))
