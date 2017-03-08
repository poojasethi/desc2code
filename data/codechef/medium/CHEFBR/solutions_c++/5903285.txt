#include <bits/stdc++.h>

using namespace std;

struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
typedef long long int Number;
const Number MOD = 1000000007;
int n;
int a[123];
Number dp[123][123];
Number solve(int i, int j) {
    if (i > j) return 1LL;
    Number &ans = dp[i][j];
    if (ans != -1) return ans;
    ans = solve(i + 1, j);
    if (a[i] < 0) //Abrir
	for (int k = i + 1; k <= j; k++)
	    if (a[k] == (-a[i])) //Cerrar
		ans = (ans + ((solve(i + 1, k - 1) * solve(k + 1, j)) % MOD)) % MOD;
    return ans;
}
int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
	scanf("%d", a + i);  
    memset(dp, -1, sizeof(dp));
    printf("%lld\n", solve(0, n - 1));
    return 0;
}
