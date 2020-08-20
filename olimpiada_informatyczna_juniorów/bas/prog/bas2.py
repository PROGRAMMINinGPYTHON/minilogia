# Wczytujemy liczbę pomiarów.
N = input()

# Wczytujemy tablice pomiarów.
# Pobrane pomiary konwertujemy z napisów na liczby.
P = [int(x) for x in input().split()]

# Zmienna określająca ile przepłynęliśmy już długości basenu (wynik).
# Pierwszy basen zaczynamy już przepływać na początku.
przeplyniete = 1
# Zmienna utrzymująca, jaka była poprzednio wskazana wartość na zegarku Bajtka.
# -1 jest dla nas wygodną wartością początkową, bo wszystkie pomiary są dodatnie.
poprzedni = -1
# Zmienna określająca, czy aktualnie oddalamy się od brzegu, czy zbliżamy do niego.
# Jak zaczynamy, to odpływamy od brzegu. Dlatego rosnący jest równe true (prawdzie).
rosnacy = True

# Dla każdego pomiaru:
for p in P:
  # jeżeli do tej pory oddalaliśmy się od brzegu, ale to się teraz zmieniło
  # (to jest nowy pomiar jest mniejszy od poprzedniego),
  if rosnacy == True and poprzedni > p:
    # to znaczy, że musieliśmy zawrócić, zatem dodajemy nowy basen
    przeplyniete += 1
    # i zmieniamy kierunek na przeciwny.
    rosnacy = False
  # Analogicznie jeżeli do tej pory zbliżaliśmy się do brzegu,
  # a nowy pomiar jest większy od poprzedniego,
  elif rosnacy == False and poprzedni < p:
    # to znaczy, że też musieliśmy odbić od brzegu, zatem zwiększamy wynik
    przeplyniete += 1
    # i zmieniamy kierunek na przeciwny.
    rosnacy = True
  # Pamiętamy, aby zaktualizować ostatni pomiar.
  poprzedni = p

# Finalnie, wypisujemy wynik - liczbę przepłyniętych basenów.
print(przeplyniete)
