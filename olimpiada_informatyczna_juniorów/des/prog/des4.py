# Pomocnicza funkcja, która zwraca indeks maksymalnego elementu tablicy L.
def znajdzMax(L, N):
  indeks_maxa = 0
  # Przechodzimy przez całą tablicę,
  for i in range(1, N):
    # jeżeli znajdziemy element tablicy większy od aktualnego maksimum,
    if L[indeks_maxa] < L[i]:
      # to aktualizujemy indeks na maksimum.
      indeks_maxa = i
  return indeks_maxa

# Wczytujemy liczbę desek.
N = int(input())

# Wczytujemy długości desek. Wszystkie elementy konwertujemy
# z napisów na liczby.
L = [int(l) for l in input().split()]

# Trzykrotnie znajdujemy maksymalny element i zamieniamy go na zero.
for i in range(3):
    indeks_maxa = znajdzMax(L, N)
    L[indeks_maxa] = 0

# Znajdujemy czwarty największy element i wypisujemy go.
# Jeżeli elementów tablicy L jest mniej niż 4, to wtedy wszystkie są
# zerami, więc odpowiedzią będzie 0, jak jest wymagane.
indeks_czwartego = znajdzMax(L, N)
print(L[indeks_czwartego] * L[indeks_czwartego])
