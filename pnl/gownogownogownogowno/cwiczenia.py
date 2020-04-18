import locale
import os
def srak(old,new):
    plik = open(old, encoding='utf-8')
    a = plik.read()
    print(a)
    plik.close()
    plik_a= open(new,encoding='utf-8',mode='w')
    plik_a.write(a)

srak('dddd','ddddd2.txt')
