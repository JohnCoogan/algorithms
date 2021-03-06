///
// String Similarity - John Coogan
// Reimplementation of Python Script to handle long inputs faster.
///


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int score_string(char a[], int b, int c) {
    int i = 0, j = 0, count = 0;
    int x = b;
    for (i = x, j = 0; i < c; i++) {
        if (a[i] == a[j++]) {
            count++;
        }
        else
            break;
    }
    return count;
}

int main() {
    int sum = 0, y = 0;
    int i = 0;
    int T = 0;
    char st[1000000];
    scanf("%d", &T);
    while(T--) {
        sum = 0;
        scanf("%s", st);
        y = strlen(st);
        for (i = 0; i < y; i++) {
            if (st[i] == st[0]) {
                sum = sum + score_string(st, i, y);   
            }
        }
        printf("%d\n", sum);
    }
    return (EXIT_SUCCESS);
}