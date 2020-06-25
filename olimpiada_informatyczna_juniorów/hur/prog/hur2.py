# Zadeklaruj i wczytaj zmienną N.
N = int(input())

# Dla każdej liczby od 1 do N:
for i in range(1, N+1):
  # sprawdzamy resztę z dzielenia przez 7 i 11.
  # Rozważamy wszystkie 4 przypadki.

  # Jeżeli liczba nie dzieli się przez 7 ani 11, po prostu ją wypisujemy.
  if i%7!=0 and i%11!=0:
    print(i)

  # Jeżeli liczba dzieli się tylko przez 7, wypisujemy "Hurra!".
  if i%7==0 and i%11!=0:
    print("Hurra!")

  # Jeżeli liczba dzieli się tylko przez 11, wypisujemy "Super!".
  if i%7!=0 and i%11==0:
    print("Super!")

  # Jeżeli liczba dzieli się zarówno przez 7, jak i 11, wypisujemy "Wiwat!".
  if i%7==0 and i%11==0:
    print("Wiwat!")
