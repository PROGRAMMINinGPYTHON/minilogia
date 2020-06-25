#include "bits/stdc++.h"

using namespace std;

int main() {
  // Wyłączenie synchronizacji. Przyśpiesza operacje wejścia/wyjścia.
  ios_base::sync_with_stdio(0);

  // Wczytujemy napis.
  string x;
  cin >> x;

  // Dla każdej litery w napisie na wejściu sprawdzamy czy musimy ją zamienić.
  int d = x.size();
  for (int i = 0; i<d; i++) {
    if (x[i] == 'a') cout << '4';
    else if (x[i] == 'e') cout << '3';
    else if (x[i] == 'i') cout << '1';
    else if (x[i] == 'o') cout << '0';
    else if (x[i] == 's') cout << '5';
    // W przeciwnym wypadku (jeżeli nie musimy jej zamienić),
    // to wypisujemy po prostu tę literę.
    else cout << x[i];
  }
}
