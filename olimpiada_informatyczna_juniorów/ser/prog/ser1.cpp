#include "bits/stdc++.h"

using namespace std;

int main() {
  // Deklarujemy zmienną N (liczbę
  // serduszek)
  int N;
  // i wczytujemy ją.
  cin >> N;

  // N razy wypisujemy pojedyncze serce.
  for (int i = 0; i < N; i++) {
    // Wypisujemy serce linijka
    // po linijce.
    cout << " @@@   @@@ " << "\n";
    cout << "@   @ @   @" << "\n";
    cout << "@    @    @" << "\n";
    cout << "@         @" << "\n";
    cout << " @       @ " << "\n";
    cout << "  @     @  " << "\n";
    cout << "   @   @   " << "\n";
    cout << "    @ @    " << "\n";
    cout << "     @     " << "\n";
  }

  return 0;
}
