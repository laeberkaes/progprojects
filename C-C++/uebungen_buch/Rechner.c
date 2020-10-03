//
// Created by fuchur on 9/12/20.
//

#include <stdio.h>
#include <string.h>

int main(void) {
    double op1, op2, erg;
    char operatorgithub;
    printf("Geben sie den ersten Operanten an: \n");
    scanf("%lf", &op1);
    printf("Geben sie den zweiten Operanten ein: \n");
    scanf("%lf", &op2);
    printf("Was soll der Operator sein?: \n");
    scanf("%c", &operator);
    if (strcmp(&operator, "+")) {
        erg = op1 + op2;
    } else if (strcmp(&operator, "-")) {
        erg = op1 - op2;
    } else if (strcmp(&operator, "*")) {
        erg = op1 * op2;
    } else if (strcmp(&operator, "/")) {
        erg = op1 / op2;
    } else {
        printf("Kein Operator!");
    }
    printf("Ergebnis: %f", erg);
    return 0;
}