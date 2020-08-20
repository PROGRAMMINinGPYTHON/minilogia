#include "bits/stdc++.h"

using namespace std;

int main() {
  // Wyłączenie synchronizacji. Przyśpiesza operacje wczytywania/wypisywania.
  ios_base::sync_with_stdio(0);

  // Deklarujemy i wczytujemy liczbe pomiarów.
  int N;
  cin >> N;

  // Zmienna określająca ile przepłynęliśmy już długości basenu (wynik).
  // Pierwszy basen zaczynamy już przepływać na początku.
  int przeplyniete = 1;
  // Zmienna utrzymująca, jaka była poprzednio wskazana wartość na zegarku Bajtka.
  // -1 jest dla nas wygodną wartością początkową, bo wszystkie pomiary są dodatnie.
  int poprzedni = -1;
  // Zmienna określająca, czy aktualnie oddalamy się od brzegu, czy zbliżamy do niego.
  // Jak zaczynamy, to odpływamy od brzegu. Dlatego rosnący jest równe true (prawdzie).
  bool rosnacy = true;

  // Musimy obsłużyć N pomiarów.
  for (int i=0; i<N; i++) {
    // Deklarujemy zmienną na pomiar i wczytujemy ją.
    int p;
    cin >> p;
    // Jeżeli do tej pory oddalaliśmy się od brzegu, ale to się teraz zmieniło
    // (to jest nowy pomiar jest mniejszy od poprzedniego),
    if (rosnacy == true && poprzedni > p) {
      // to znaczy, że musieliśmy zawrócić, zatem dodajemy nowy basen
      przeplyniete++;
      // i zmieniamy kierunek na przeciwny.
      rosnacy = false;
    // Analogicznie jeżeli do tej pory zbliżaliśmy się do brzegu,
    // a nowy pomiar jest większy od poprzedniego,
    } else if (rosnacy == false && poprzedni < p) {
      // to znaczy, że też musieliśmy odbić od brzegu, zatem zwiększamy wynik
      przeplyniete++;
      // i zmieniamy kierunek na przeciwny.
      rosnacy = true;
    }
    // Pamiętamy, aby zaktualizować ostatni pomiar.
    poprzedni = p;
  }

  // Finalnie, wypisujemy wynik - liczbę przepłyniętych basenów.
  cout << przeplyniete << "\n";
}
