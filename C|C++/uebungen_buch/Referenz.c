#include <stdio.h>

void add(int zahl1, int *zahl2) {
  zahl1 += 17;
  *zahl2 +=15;
}

int main(void)
{
  int zahl1 = 0;
  int zahl2 = 0;
  printf("Zahl1 = %d\n", zahl1);
  printf("Zahl2 = %d\n", zahl2);
  add(zahl1, &zahl2);
  printf("Zahl1 = %d\n", zahl1);
  printf("Zahl2 = %d\n", zahl2);
  getchar();
  return 0;
}
