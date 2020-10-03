#include <stdio.h>

const signed int kelv_const = -273;

int main(void) {
  signed int deg;
  printf("Gib eine Zahl ein, die in Kelvin umgewandelt werdne soll:\n> ");
  scanf("%i", &deg);
  printf("%i\n", deg+kelv_const);
  return 0;
}
