#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
typedef long long Int;
#define MOD (1000000007LL)

Int dp[2][2];

int main() {
    string a, b;
    int K;
    cin >> a >> b >> K;
    const int n = a.size();
    Int *cur = dp[0], *nxt = dp[1];
    cur[0] = 1;
    rep (_, K) {
        nxt[0] = (n-1)*cur[1] % MOD;
        nxt[1] = (cur[0] + (n-2)*cur[1]) % MOD;
        swap(cur, nxt);
    }
    Int ans = 0;
    rep (i, n) {
        if (a == b) ans = (ans + cur[i>0]) % MOD;
        b = b.substr(1) + b[0];
    }
    cout << ans << endl;
    return 0;
}
