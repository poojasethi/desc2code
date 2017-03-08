#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 128;

char s[MAXN * 2];
int n, m, cc, c[MAXN * 2];
long long k, dp[MAXN * 2][MAXN * 2];

int main() {
	while (cin >> n >> m >> k) {
		memset(c, 0x3f, sizeof(c));
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) {
				scanf("%d", &cc);
				c[i + j - 1] = min(c[i + j - 1], cc);
			}
		}
		int nn = n + m - 1;
		vector< pair<int, int> > p;
		for (int i = 1; i <= nn; ++i)
			p.push_back(make_pair(c[i], i));
		sort(p.begin(), p.end());
		for (int i = 1; i <= nn; ++i)
			s[i] = '?';
		for (int pi = 0; pi < nn; ++pi) {
			s[p[pi].second] = '(';
			memset(dp, 0, sizeof(dp));
			dp[0][0] = 1;
			for (int i = 0; i < nn; ++i) {
				for (int j = 0; j <= i; ++j) {
					if (dp[i][j] > 0) {
						if (s[i + 1] != ')' && dp[i + 1][j + 1] < k) {
							dp[i + 1][j + 1] += dp[i][j];
						}
						if (s[i + 1] != '(' && j > 0 && dp[i + 1][j - 1] < k) {
							dp[i + 1][j - 1] += dp[i][j];
						}
					}
				}
			}
			if (dp[nn][0] < k) {
				s[p[pi].second] = ')';
				k -= dp[nn][0];
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j)
				putchar(s[i + j - 1]);
			putchar('\n');
		}
	}
	return 0;
}
