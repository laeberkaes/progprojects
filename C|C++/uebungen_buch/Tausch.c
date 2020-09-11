//
// Created by fuchur on 9/11/20.
//

#include <stdio.h>

void tausch(int a, int b);

int a;
int b;

int main() {
    a = 2;
    b = 3;
    printf("%d", a);
    printf("%d\n", b);
    tausch(a, b);
    printf("%d", a);
    printf("%d\n", b);
    return 0;
}

void tausch(int d, int e) {
    int c = a;
    a = b;
    b = c;
}