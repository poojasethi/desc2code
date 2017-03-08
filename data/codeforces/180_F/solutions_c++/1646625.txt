#include <stdio.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int n, a[200000], b[200000], c[200000];

int main() {
    scanf("%d", &n);
    rep (i, n) scanf("%d", a+i);
    rep (i, n) scanf("%d", b+i);
    rep (i, n) c[a[i]] = b[i];
    rep (i, n) printf("%d%c", c[i+1], "\n "[i<n-1]);
    return 0;
}
