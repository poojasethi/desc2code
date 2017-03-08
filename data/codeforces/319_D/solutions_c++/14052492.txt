#include <stdio.h>
#include <string.h>

char s[60000];

int main() {
    scanf("%s", s);
    int n = strlen(s);
    for (int L = 1; L <= n/2; L++) {
        int m = L;
        for (int i = L, k = 0; i < n; i++) {
            k = s[i] == s[i-L] ? k+1 : 0;
            if (k == L) m -= L, k = 0;
            s[m++] = s[i];
        }
        n = m;
    }
    s[n] = 0;
    puts(s);
    return 0;
}
