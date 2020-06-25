# Wczytujemy napis.

x = input()

wynik = ""

for litera in x:
  if litera == 'a': wynik += '4'
  elif litera == 'e': wynik += '3'
  elif litera == 'i': wynik += '1'
  elif litera == 'o': wynik += '0'
  elif litera == 's': wynik += '5'
  else: wynik += litera

# Wypisujemy wynik.
print(wynik)
