#include "bits/stdc++.h"

using namespace std;

// Dobrym zwyczajem algorytmicznym jest ustawienie
// rozmiaru tablicy na troche wiekszy niz wymagany.
const int MAX_N = 1000 * 1000 + 5;

int L[MAX_N];

// Pomocnicza funkcja, która zwraca indeks maksymalnego elementu tablicy L.
int znajdzMax(int N) {
  int indeks_maxa = 0;
  // Przechodzimy przez całą tablicę,
  for (int i=1; i<N; i++) {
    // jeżeli znajdziemy element tablicy większy od aktualnego maksimum,
    if (L[indeks_maxa] < L[i]) {
      // to aktualizujemy indeks na maksimum.
      indeks_maxa = i;
    }
  }
  return indeks_maxa;
}

int main() {
  ios_base::sync_with_stdio(0);

  // Deklarujemy i wczytujemy zmienną N - liczbę desek,
  int N;
  cin >> N;

  // a następnie same długości desek do tablicy L.
  for (int i = 0; i < N; ++i) {
    cin >> L[i];
  }

  // Trzykrotnie znajdujemy maksymalny element i zamieniamy go na zero.
  for (int i=0; i<3; i++) {
    int indeks_maxa = znajdzMax(N);
    L[indeks_maxa] = 0;
  }

  // Znajdujemy czwarty największy element i wypisujemy go.
  // Jeżeli elementów tablicy L jest mniej niż 4, to wtedy wszystkie są
  // zerami, więc odpowiedzią będzie 0, jak jest wymagane.
  int indeks_czwartego = znajdzMax(N);
  cout << (long long)L[indeks_czwartego] * L[indeks_czwartego] << "\n";
}
