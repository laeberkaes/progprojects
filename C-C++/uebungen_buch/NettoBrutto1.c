#include <stdio.h>

const double mwst_satz = 0.19;
const double artikel_1 = 7.20;
const double artikel_2 = 1.40;
const double artikel_3 = 5.60;
double preis;

void add_mwst(void) {
  printf("\n+\t%f EUR\n", preis * (mwst_satz+1));
}

int main(void) {
  preis = artikel_1;
  add_mwst();
  preis = artikel_2;
  add_mwst();
  preis = artikel_3;
  add_mwst();
  printf("----------\n");
  preis = artikel_1 + artikel_2 + artikel_3;
  add_mwst();
  printf("==========\n");
  getchar();
  return 0;
}
