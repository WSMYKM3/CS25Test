#include <cs50.h>//here I have not install the cs50 library
#include <stdio.h>

int main(void)
{
    string name = get_string(What's your name?\n");
    printf("hello ,%s\n", name);
    return 0;
}
