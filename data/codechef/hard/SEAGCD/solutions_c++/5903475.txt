#include <bits/stdc++.h>

using namespace std;

struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
typedef long long int Number;
const Number MOD = 1000000007LL;
Number N, M, L, R;
int b[10000009];
Number modpow(Number base, Number e) {
    if (e == 0) return 1LL;
    Number ans = modpow(base, e / 2LL);
    ans = (ans * ans);
    if (ans >= MOD) ans %= MOD;
    if (e & 1LL) ans = ans * base;
    if (ans >= MOD) ans %= MOD;
    return ans;
}
int solve() {
    int num, ult = -1, expo, div, ans = 0;
    for (int D = M; D >= L; D--) {
	div = M / D;
	if (div == ult)
	    b[D] = expo;
	else {
	    expo =  modpow(div, N);
	    b[D] = expo;
	    ult = div;
	}
	
	num = D + D;
	while (num <= M) {
	    b[D] = (b[D] - b[num]);
	    if (b[D] < 0) b[D] += MOD;
	    num += D;
	}
	if (D <= R) {
	    ans = (ans + b[D]);
	    if (ans >= MOD) ans -= MOD;
	}
    }
    if (ans < 0) ans += MOD;
    return ans;
}
int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
	scanf("%lld %lld %lld %lld", &N, &M, &L, &R);
	printf("%d\n", solve());
    }
    return 0;
}
