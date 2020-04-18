import locale
import os
def nadpisanie():
    plik=open('dddd',encoding='utf-8',mode='w')
    for x in range(10):
        plik.write(str(x)+"\n")
    linie = []
    for x in range(10):
        linie.append("linia numer {} \n".format(x))
    plik.writelines(linie)
    plik= open('dddd',encoding='utf-8')
    linie=plik.read()
    print(linie)
def dopisanie():
    plik = open('nowy.txt', encoding='utf-8', mode='a')

def czytanie_i_pisanie():
    plik = open('nowy.txt', encoding='utf-8', mode='r+')

nadpisanie()