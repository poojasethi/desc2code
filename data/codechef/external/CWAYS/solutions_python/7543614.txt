#include <bits/stdc++.h>

// #pragma comment(linker, "/STACK:16777216")

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

#define filla(a, x) memset(a, x, sizeof(a))
#define fillv(v, x) memset(&v[0], x, v.size() * sizeof(v[0]))
#define foreach(it, x) for(__typeof(x.begin()) it = x.begin(); it != x.end(); it++)
#define sqr(x) ((x)*(x))

inline int read() {   int x;   scanf("%d",&x);   return x;   }
inline int readln() {   int x;   scanf("%d\n",&x);   return x;   }


const int MAX_H = 2*(1e5 + 5);
const int MAX_N = 2e3 + 33;
const ll MODULE = 1e9 + 7;


int n, h, w;
pii a[MAX_N];
ll fac[MAX_H], inv[MAX_H], f[MAX_N];


ll mpow(ll x, ll d) {
	if (d < 1) return 1;
	if (d == 1) return x % MODULE;
	ll t = mpow(x, d>>1);
	t = (t*t) % MODULE;
	if (d&1) return (t*x) % MODULE;
	return t;
}


inline ll getC(int n, int k) {
	if (k < 0 || k > n) return 0;
	if (k == 0 || k == n) return 1;
	ll ans = fac[n];
	ans = (ans * inv[k]) % MODULE;
	ans = (ans * inv[n-k]) % MODULE;
	return ans;
}


inline ll cal(int i, int j) {
	ll m = a[j].first - a[i].first + 1;
	ll n = a[j].second - a[i].second + 1;
	return getC(m+n-2, m-1);
}


int main() {
#ifdef DEBUG
	freopen("CWAYS.in", "r", stdin);
	freopen("CWAYS.out", "w", stdout);
#endif
	fac[0] = inv[0] = 1;
	for (int i = 1; i < MAX_H; ++i) {
		fac[i] = (fac[i-1] * i) % MODULE;
		inv[i] = mpow(fac[i], MODULE-2);
	}

	int nTest = read();
	while (nTest--) {
		scanf("%d%d%d", &h, &w, &n);
		for (int i = 1; i <= n; ++i)
			scanf("%d%d", &a[i].first, &a[i].second);
		a[0] = pii(1, 1);
		a[++n] = pii(h, w);
		sort(a+1, a+1+n);

		for (int i = 1; i <= n; ++i)
			f[i] = cal(0, i);
		for (int i = 1; i < n; ++i)
			for (int j = i+1; j <= n; ++j) {
				if (a[j].first < a[i].first || a[j].second < a[i].second)
					continue;
				f[j] = (f[j] - f[i] * cal(i, j)) % MODULE;
				if (f[j] < 0) f[j] += MODULE;
			}
		printf("%lld\n", f[n]);
	}
	return 0;
}