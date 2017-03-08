#include <stdio.h>
#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define MOD (1000000007LL)
typedef long long Int;

int n, L, a[2][128], r[128];
Int dp[4096][128][2];

int main() {
    scanf("%d%d", &n, &L);
    rep (i, n) scanf("%d%d", a[0]+i, a[1]+i);
    rep (i, n) r[i] = a[0][i] == a[1][i] ? 1 : 2;
    rep (i, n) rep (d, r[i]) {
        dp[a[1-d][i]][i][d] = 1;
    }
    rep (k, L) rep (i, n) rep (x, r[i]) {
        rep (j, n) if (i != j) rep (y, r[j]) {
            if (a[x][i] == a[1-y][j]) {
                dp[k+a[1-y][j]][j][y] += dp[k][i][x];
                dp[k+a[1-y][j]][j][y] %= MOD;
            }
        }
    }
    Int ans = 0;
    rep (i, n) ans = (ans + dp[L][i][0] + dp[L][i][1]) % MOD;
    cout << ans << endl;
    return 0;
}

