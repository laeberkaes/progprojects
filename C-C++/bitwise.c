#include <stdio.h>
int main(void) {
  int e, x = 9;
  printf("Ausgabe Ausgangswert: %d\n", x);
  e = x & 3;
  printf("Ausgabe UND-Verknuepfung mit 3: %d\n", e);
  e = x | 3;
  printf("Ausgabe ODER-Verknuepfung mit 3: %d\n", e);
  e = x ^ 3;
  printf("Ausgabe EXCLUSIV-ODER-Verknuepfung mit 3: %d\n", e);
  e = x << 1;
  printf("Ausgabe Linksschieben um 1 Stelle: %d\n", e);
  e = x >> 3;
  printf("Ausgabe Rechtsschieben um 3 Stellen: %d\n", e);
  e =~ x;
  printf("Das unaere Komplement ist: %d\n", e);
  getchar();
  return 0;
}
