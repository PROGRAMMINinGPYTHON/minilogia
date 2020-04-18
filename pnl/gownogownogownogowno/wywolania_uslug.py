import requests
odpowiedz=requests.get("http://jsystems.pl/static/blog/python/dane.json",auth=('user','pass'))
print(odpowiedz.status_code)
dane = odpowiedz.json()
print(dane)

odpowiedz=requests.get("http://owocek.cba.pl")
print("strona: ")
print(type(odpowiedz))
print(odpowiedz.text)

posty = requests.get("https://jsonplaceholder.typicode.com/posts").json()
print (posty[0])
print (posty[0]["body"])