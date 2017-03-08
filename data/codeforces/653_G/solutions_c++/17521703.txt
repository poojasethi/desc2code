#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;
const LL MOD = 1000000007;

LL mul(LL a, LL b) { return a * b % MOD; }

void add(LL& a, LL b) { a += b; if(a >= MOD) a -= MOD; }

void sub(LL& a, LL b) { a -= b; if(a < 0) a += MOD; }

LL pow_mod(LL a, int p) {
	LL ans = 1;
	while(p) {
		if(p & 1) ans = mul(ans, a);
		a = mul(a, a);
		p >>= 1;
	}
	return ans;
}

const int maxn = 300000 + 10;
const int maxp = 26000;

bool vis[maxn];
int prime[maxp], pid[maxn], pcnt;

void preprocess() {
	for(int i = 2; i < maxn; i++) {
		if(!vis[i]) { prime[pcnt] = i; pid[i] = pcnt++; }
		for(int j = 0; j < pcnt; j++) {
			if(i * prime[j] >= maxn) break;
			vis[i * prime[j]] = true;
			if(i % prime[j] == 0) break;
		}
	}
}

int n, a[maxn];
int cnt[maxp][20];

LL fac[maxn], inv[maxn], Cn[maxn];

void decompose(int x) {
	for(int i = 0; x > 1; i++) {
		int p = prime[i];
		if(p * p > x) break;
		if(x % p != 0) continue;
		int e = 0;
		while(x % p == 0) { x /= p; e++; }
		cnt[i][e]++;
	}
	if(x > 1) cnt[pid[x]][1]++;
}

int main()
{
	preprocess();

	scanf("%d", &n);
	for(int i = 1; i <= n; i++) scanf("%d", a + i);

	fac[0] = 1;
	for(int i = 1; i <= n; i++) fac[i] = mul(fac[i - 1], i);
	inv[n] = pow_mod(fac[n], MOD - 2);
	for(int i = n - 1; i >= 0; i--) inv[i] = mul(inv[i + 1], i + 1);
	for(int i = 0; i <= n; i++) Cn[i] = mul(mul(fac[n], inv[i]), inv[n - i]);
	for(int i = 1; i <= n; i++) add(Cn[i], Cn[i - 1]);
	for(int i = 1; i <= n; i++) add(Cn[i], Cn[i - 1]);

	for(int i = 1; i <= n; i++) decompose(a[i]);

	LL ans = 0;
	LL S = pow_mod(2, n - 1);
	for(int i = 0; i < pcnt; i++) {
		int tot = n;
		for(int j = 1; j < 20; j++) tot -= cnt[i][j];
		for(int j = 1; j < 20; j++) if(cnt[i][j]) {
			int L = tot, R = L + cnt[i][j] - 1;
			tot += cnt[i][j];
			LL t = Cn[R];
			if(L) sub(t, Cn[L - 1]);
			sub(t, mul(S, cnt[i][j]));
			add(ans, mul(t, j));
		}
	}

	printf("%lld\n", ans);

	return 0;
}
