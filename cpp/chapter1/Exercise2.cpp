void run(char *str)
{
    int i = -1;
    char a;
    do {
        i++;
        a = str[i];
    } while (a != '\0');

    for (int j = 0; j < i/2; j++) {
        char tempChar = str[j];
        str[j] = str[i-j-1];
        str[i-j-1] = tempChar;
    }
}
