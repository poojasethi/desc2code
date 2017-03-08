#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long ll;
const int N = 1000010;
int factor[N], invf[N];
int ans;
int MOD = 1000000007;
int quick_inverse(int n, int p) {
    int ret = 1;
    int exponent = p - 2;
    for (int i = exponent; i; i >>= 1, n = 1ll * n * n % p) {
	if (i & 1) {
	    ret = 1ll * ret * n % p;
	}
    } 
    return ret;
}
int mp[N], kp[N];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    factor[0] = 1;
    for (int i = 1; i < N; ++i) {
	factor[i] = 1ll * i * factor[i - 1] % MOD;
    }
    invf[N - 1] = quick_inverse(factor[N - 1], MOD);
    for (int i = N - 2; i >= 0; --i) {
	invf[i] = 1ll * invf[i + 1] * (i + 1) % MOD;
    }
    mp[0] = kp[0] = 1;
    for (int i = 1; i < N; ++ i) {
	mp[i] = 1ll * mp[i - 1] * m % MOD;
	kp[i] = 1ll * kp[i - 1] * (m - 1) % MOD;
    }
    int ans = mp[n];
    for (int i = 1; i <= n; ++ i) {
	int tmp = 1ll * factor[n] * invf[i - 1] % MOD * invf[n - i + 1] % MOD;
	tmp = 1ll * tmp * mp[i] % MOD;
	tmp = 1ll * tmp * kp[n - i] % MOD;
	ans = (ans + tmp) % MOD;
    }
    printf("%d\n", ans);
    return 0;
}
