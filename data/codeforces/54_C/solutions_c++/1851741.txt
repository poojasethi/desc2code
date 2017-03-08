#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 1024;

int n, k;
long long l, r;
double dp[MAXN][MAXN];

inline double getP(long long l, long long r) {
	long long cnt = 0, p = 1, tl, tr;
	while (p <= r) {
		tl = p;
		tr = p * 2 - 1;
		tl = max(tl, l);
		tr = min(tr, r);
		if (tl <= tr)
			cnt += tr - tl + 1;
		if (p > r / 10)
			break;
		p *= 10;
	}
	return 1.0 * cnt / (r - l + 1);
}

int main() {
	while (cin >> n) {
		for (int i = 0; i <= n; ++i)
			memset(dp[i], 0, sizeof(dp[0][0]) * (n + 1));
		dp[0][0] = 1.0;
		for (int i = 1; i <= n; ++i) {
			cin >> l >> r;
			double p = getP(l, r);
			for (int j = 0; j <= i; ++j) {
				if (j > 0)
					dp[i][j] += p * dp[i - 1][j - 1];
				dp[i][j] += (1.0 - p) * dp[i - 1][j];
			}
		}
		cin >> k;
		double ans = 0.0;
		for (int j = 0; j <= n; ++j) {
			if (j * 100 >= k * n)
				ans += dp[n][j];
		}
		printf("%.10lf\n", ans);
	}
	return 0;
}
