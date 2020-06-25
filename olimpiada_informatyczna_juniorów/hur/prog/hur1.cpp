#include "bits/stdc++.h"

using namespace std;

int main() {
  // Wyłączamy synchronizację, przyśpiesza operacje wejścia/wyjścia.
  ios_base::sync_with_stdio(0);

  // Zadeklaruj i wczytaj zmienną N.
  int N;
  cin >> N;

  // Dla każdej liczby od 1 do N:
  for (int i=1; i<=N; i++) {
    // sprawdzamy resztę z dzielenia przez 7 i 11.
    // Rozważamy wszystkie 4 przypadki.

    // Jeżeli liczba nie dzieli się przez 7 ani 11, po prostu ją wypisujemy.
    if (i%7!=0 && i%11!=0) {
      cout << i << "\n";
    }

    // Jeżeli liczba dzieli się tylko przez 7, wypisujemy "Hurra!".
    if (i%7==0 && i%11!=0) {
      cout << "Hurra!" << "\n";
    }

    // Jeżeli liczba dzieli się tylko przez 11, wypisujemy "Super!".
    if (i%7!=0 && i%11==0) {
      cout << "Super!" << "\n";
    }

    // Jeżeli liczba dzieli się zarówno przez 7, jak i 11, wypisujemy "Wiwat!".
    if (i%7==0 && i%11==0) {
      cout << "Wiwat!" << "\n";
    }
  }
}
