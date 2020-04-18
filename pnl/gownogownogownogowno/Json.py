import json
plik= open('dane.json',encoding='utf-8')
obj = json.load(plik)
print(obj)
print(type(obj))
plik.close()
print (obj['imie'])
print (obj['adres']['kod'])
print (obj['jezyki'][2])

for k in obj.keys():
    print(k, " -> ", obj[k])

obj=dict()
obj['ksiazka']='Finansowy Ninja'
obj['film_na_wieczor']='https://www.youtube.com/watch?v=sCNrK-n68CM'
obj['banknoty']=[10,20,50,100,200,500]
plik=open('jsonout.json',encoding='utf-8',mode="w")
json.dump(obj,plik)
plik.close()