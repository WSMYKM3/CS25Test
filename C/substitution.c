#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool is_valid_key(string key);

// check for arguements' number
int main(int argc, string argv[])
{
    // Check argument count
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];

    // Validate key
    if (!is_valid_key(key))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }

    // output plaintext: (without a newline) and then prompt the user for a string of plaintext
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    // Encrypt
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];
        if (isupper(c))
        {
            int index = c - 'A'; // position in alphabet
            char encrypted = toupper(key[index]);
            printf("%c", encrypted);
        }
        else if (islower(c))
        {
            int index = c - 'a';
            char encrypted = tolower(key[index]);
            printf("%c", encrypted);
        }
        else
        {
            printf("%c", c); // non-alphabetic unchanged
        }
    }

    // After outputting ciphertext, print a newline. Your program should then exit by returning 0
    // from main
    printf("\n");
    return 0;
}

// Function to validate key
bool is_valid_key(string key)
{
    // Must be 26 chars, or quit immediately
    if (strlen(key) != 26)
    {
        return false;
    }

    // setup a initializer,check for repeated letter, when first find it, set to true, then if
    // (seen[index]) indicates it already true,which means that time it is a repeated letter
    bool seen[26] = {false};

    // make sure alphabetic character
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        // using ASCII distance to check if
        int index = toupper(key[i]) - 'A';
        // if (seen[index]) means seen[index] already true
        if (seen[index])
        {
            return false; // check repeated letter
        }
        seen[index] = true;
    }

    return true;
}
