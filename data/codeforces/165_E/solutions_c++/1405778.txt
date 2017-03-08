#include <stdio.h>
#include <string.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

#define N (1<<22)
int n, a[N], dp[N];

int main() {
    scanf("%d", &n);
    rep (i, n) scanf("%d", a+i);
    memset(dp, -1, sizeof(dp));
    rep (i, n) dp[a[i]] = a[i];
    rep (b, N) if (dp[b] != -1) {
        rep (i, 22) dp[b|(1<<i)] = dp[b];
    }
    rep (i, n) printf("%d%c", dp[(N-1)^a[i]], i+1<n?' ':'\n');
    return 0;
}
