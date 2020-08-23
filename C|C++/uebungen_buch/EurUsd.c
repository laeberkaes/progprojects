#include <stdio.h>

const double usd_kurs = 1.13681;
double artikelpreis;
double ergebnis;
double eur_usd(double preis) {
  return preis*usd_kurs;
}

int main(void) {
  printf("Gib einen Preis in EUR an, der in USD umgerechnet werden soll:\n> ");
  scanf("%lf", &artikelpreis);
  printf("%lf\n", eur_usd(artikelpreis));
  return 0;
}
