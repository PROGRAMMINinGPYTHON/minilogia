import locale
import os

def wielkosc_pliku():
    ile=os.path.getsize('dddd')
    print(ile)
    print("wynik w bajtach")

def srakasraka():
    print(locale.getpreferredencoding())
    plik = open('dddd', encoding='utf-8')
    pl = open('dddd', encoding='utf-8')
    linie = pl.read()
    plik.close()
    print(linie)
    # print(type(linie))
    # plik = open('ddd.py',encoding='utf-8')
    # pl = open('ddd.py',encoding='utf-8')
    # linie = pl.read()
    # plik.close()
    # print(linie)
    # linie = pl.read()

def odczyt(ile):
    plik = open('dddd', encoding='utf-8')
    linie = plik.read(ile)
    print("---------XXX----------")
    print(linie)
    print("---------XXX----------")
    print(linie)
    print("---------XXX----------")

def redloty_inne():
    pl = open('dddd', encoding='utf-8')
    linie = pl.read().splitlines()
    pl.close()
    print(linie)
    print(type(linie))
    print("XXXXXXXX")

def redloty():
    pl = open('dddd', encoding='utf-8')
    linie = pl.readlines()
    pl.close()
    print(linie)
    print(type(linie))
    print("XXXXXXXXX")

def redlinia():
    with open('dddd', encoding='utf-8') as f:
        for i in f:
            print(i)
        print("XXXXX")


def seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeek():
    print("seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeek")
    plik = open('dddd', encoding='utf-8')
    linie = plik.readlines()
    print(linie)
    plik.seek(20)
    linie = plik.readlines()
    print(linie)
    plik.close()

seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeek()

def seeeek_inne():
    print("seeek2")
    plik = open('dddd',encoding='utf-8')
    linie = plik.readlines()
    for i in range(2):
         print(linie)
    # plik.seek(0)
    # print(linie)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def lenn():
    plik = open('dddd', encoding='utf-8')
    linie = plik.readlines()
    print('liczba wierszy w pliku={}'.format(len(linie)))
    plik.close()
# wielkosc_pliku()
# srakasraka()
# odczyt(20)
# redloty()
# redloty_inne()
# redlinia()
# seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeek()
# seeeek_inne()
# lenn()