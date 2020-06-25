# Wczytujemy napis.
x = input()

# Definiujemy wynik - napis, który będziemy tworzyć.
wynik = ""

# Dla każdej litery w napisie na wejściu sprawdzamy czy musimy ją zamienić.
for litera in x:
  if litera == 'a': wynik += '4'
  elif litera == 'e': wynik += '3'
  elif litera == 'i': wynik += '1'
  elif litera == 'o': wynik += '0'
  elif litera == 's': wynik += '5'
  # W przeciwnym wypadku (jeżeli nie musimy jej zamienić)
  # to wypisujemy po prostu tę literę.
  else: wynik += litera

# Wypisujemy wynik.
print(wynik)
