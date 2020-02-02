
import narzedzia as n
from narzedzia import *


def test_sumuj():
    assert sumuj(5,3)==8

def test_sumuj2():
    assert n.sumuj(2,6)==8
    assert n.sumuj(3,3) == 6
    assert n.sumuj(2,2) == 4
    assert n.sumuj(2,3) == 5
    assert n.sumuj(4,4) == 8


def test_sumuj3():
    assert n.sumuj(1,4) == 5

def test_sumuj4():
    print("hello ")
    assert n.sumuj(7,8) == 15



def test_opis1():
    michal = Osoba(12,"61a")
    michal.imie = "Michal"
    assert michal.opis("czerwone") == "Wygladam wspaniale, Michal .Kowalski mam oczy: czerwone zarabiam 12"
    #assert michal.__prywatnyOpis("czerwone") == "Michal .Kowalski mam oczy: czerwone zarabiam 12"
