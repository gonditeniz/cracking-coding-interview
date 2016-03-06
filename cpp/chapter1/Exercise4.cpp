#include <iostream>
using namespace std;

void run(char* str, int length)
{
    int spaceCount = 0;
    int i;
    for(i = length-1; i >= 0; i--) {
        if (str[i] == ' ') {
            spaceCount++;
        }
    }
    int newLen = length + spaceCount*2;
    str[newLen]='\0';
    for(i = length-1; i >= 0; i--) {
        newLen--;
        if (str[i] == ' ') {
            str[newLen] = '0';
            newLen--;
            str[newLen] = '2';
            newLen--;
            str[newLen] = '%';
        } else {
            str[newLen] = str[i];
        }
    }
}
