//
// Created by fuchur on 9/11/20.
//

#include <stdio.h>

double lohnsteuer(double gehalt);
double rentenversicherung(double gehalt);
double krankenversicherung(double gehalt);

double gehalt;

int main() {
    gehalt = 2500.0;
    printf("Lohnsteuer: %f\n", lohnsteuer(gehalt));
    printf("Rentenversicherung: %f\n", rentenversicherung(gehalt));
    printf("Krankenversicherung: %f\n", krankenversicherung(gehalt));
    printf("Gehalt (brutto): %f\n", gehalt);
    printf("Gehalt (netto): %f", gehalt - lohnsteuer(gehalt) - rentenversicherung(gehalt) - krankenversicherung(gehalt));
}

double lohnsteuer(double geh) {
//    double ls = geh * 0.2;
//    printf("Lohnsteuer: %f\n", ls);
    return geh * 0.2;
}

double rentenversicherung(double geh) {
//    double rv = geh * 0.1;
//    printf("Rentenversicherung: %f\n", rv);
    return geh * 0.1;
}

double krankenversicherung(double geh) {
//    double kv = geh * 0.05;
//    printf("Krankenversicherung: %f\n", kv);
    return geh * 0.05;
}