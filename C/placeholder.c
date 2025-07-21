#include <stdio.h>

int main(void) {
    char *str = "afhahf";

    for (int i = 1; i <= 6; i++) {
        printf("%.*s\n", i, str);
    }

    return 0;
}

// %s: Print a string.

// .*: The * is a dynamic precision specifier for strings.

// \n: Newline character.

//this is an example using placeholder which shows the word from left to right 
//the output will be a
// af
// afh
// afha
// afhah
// afhahf
