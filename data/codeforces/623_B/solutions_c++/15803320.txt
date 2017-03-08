#include <cstdio>

const int N = 1000001;
const long long INF = ~0ull >> 2;

int mpf[N], p[N], pn;
int n, a, b;
int c[N];
long long ans = INF;
long long dp0[N], dp1[N], dp2[N];

inline void update(long long &a, long long b) {
	if (a > b) {
		a = b;
	}
}
void test(int d, int c[], int e) {
	for (int i = 1; i < n; i++) {
		dp0[i] = dp1[i] = dp2[i] = INF;
		int t = c[i] % d;
		if (t == 0) {
			update(dp0[i], dp0[i - 1]);
			update(dp2[i], dp2[i - 1]);
		} else if (t == 1 || t == d - 1) {
			update(dp0[i], dp0[i - 1] + b);
			update(dp2[i], dp2[i - 1] + b);
		}
		update(dp1[i], dp1[i - 1] + a);
		update(dp1[i], dp0[i]);
		update(dp2[i], dp1[i]);
	}
	update(ans, e + dp2[n - 1]);
}
void cal(int x, int c[], int e) {
	for (int i = 0; i < pn; i++) {
		while (x % p[i] == 0) {
			test(p[i], c, e);
			x /= p[i];
		}
	}
	if (x != 1) {
		test(x, c, e);
	}
}
int main() {
	for (int i = 2; i < N; i++) {
		if (mpf[i] == 0) {
			mpf[i] = p[pn++] = i;
		} else {
			for (int j = 0; j < pn && i * p[j] < N && p[j] < mpf[i]; j++) {
				mpf[i * p[j]] = p[j];
			}
		}
	}
	scanf("%d%d%d", &n, &a, &b);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &c[i]);
	}
	cal(c[1], c + 1, 0);
	cal(c[1] + 1, c + 1, b);
	cal(c[1] - 1, c + 1, b);
	cal(c[n], c, 0);
	cal(c[n] + 1, c, b);
	cal(c[n] - 1, c, b);
	printf("%I64d\n", ans);
	return 0;
}
