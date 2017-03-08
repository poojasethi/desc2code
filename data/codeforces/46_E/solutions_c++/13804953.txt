#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1501;

long long maxi;
long long n, m, s[MAXN][MAXN], dp[MAXN][MAXN];

int main() {
	while (scanf("%I64d%I64d", &n, &m) != EOF) {
		for (int i = 0; i <= n; ++i)
			s[i][0] = 0;
		for (int j = 0; j <= m; ++j)
			s[0][j] = 0;
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) {
				scanf("%I64d", &s[i][j]);
				s[i][j] += s[i][j - 1];
			}
		}
		memset(dp[0], 0, sizeof(long long) * (m + 1));
		for (int i = 1; i <= n; ++i) {
			maxi = -1LL * n * m * 11000;
			if (i & 1) {
				for (int j = 1; j <= m; ++j) {
					dp[i][j] = s[i][j] + maxi;
					maxi = max(maxi, dp[i - 1][j]);
				}
			} else {
				for (int j = m; j >= 1; --j) {
					dp[i][j] = s[i][j] + maxi;
					maxi = max(maxi, dp[i - 1][j]);
				}		
			}
		}
		maxi = -1LL * n * m * 11000;
		for (int j = 1; j <= m; ++j)
			maxi = max(maxi, dp[n][j]);
		printf("%I64d\n", maxi);
	}
	return 0;
}
