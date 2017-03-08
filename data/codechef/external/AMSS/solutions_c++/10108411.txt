#include <bits/stdc++.h>

using namespace std;

#define mem(a, v) memset(a, v, sizeof (a))
#define x first
#define y second
#define all(a) (a).begin(), (a).end()
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
#define rep(i, n) for (int i = 0; i < int(n); i ++)
#define repi(i, a, n) for (int i = (a); i < int(n); i ++)
#define repe(x, v) for (auto x: (v))

int pwr[5005] = {1};
int mod = 1e9+7;
int dp[5005][5005];

int main () {
    std::ios_base::sync_with_stdio(false);
    repi(i, 1, 5005) {
        dp[i][1] = 1;
        repi(j, 2, i+1) {
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j];
            if (dp[i][j] >= mod) {
                dp[i][j] -= mod;
            }
        }
    }
    repi(j, 1, 5005) {
        repi(i, j+1, 5005) {
            dp[i][j] += dp[i-1][j];
            dp[i][j] %= mod;
        }
    }
    repi(i, 1, 5005) {
        pwr[i] = 25ll*pwr[i-1]%mod;
    }
    int tst;
    cin >> tst;
    while (tst --) {
        int ans = 0, n;
        cin >> n;
        repi(i, 1, n+1) {
            ans += 1ll*dp[n][i]*dp[n][i]%mod*pwr[i-1]%mod*26%mod;
            ans %= mod;
        }
        cout << ans << "\n";
    }
    return 0;
}
