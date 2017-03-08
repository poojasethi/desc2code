#include <bits/stdc++.h>
using namespace std;

char c[1000005];
char ans[1000005];
int ia[3][1000005];

int main () {
    int n, k;
    scanf (" %d %d", &n, &k);
    scanf (" %s", c);
    for (int i = 0; i < n/k; i++) {
        for (int j = 0; j < k; j++) {
            int index = j + k*i;
            ia[c[index]-'a'][j]++;
        }
    }
    int l = 0;
    for (int j = 0; j < k; j++) {
        for (int i = 0; i < 3; i++)
            if (ia[i][j] > l) l = ia[i][j], ans[j] = 'a' + i;
        l = 0;
    }
    printf ("%s\n", ans);
}
