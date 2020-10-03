//
// Created by fuchur on 9/12/20.
//

#include <stdio.h>

char s[9];

int main(void) {
    for (int i = 0; i < 10; ++i) {
        s[i] = getchar();
    }
    for (int i = 9; i >= 0 ; --i) {
        putchar(s[i]);
    }
}