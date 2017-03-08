#include <cstdio>
using namespace std;
inline int read() {
	char ch = getchar(); int x = 0;
	while(ch < '0' || ch > '9') ch = getchar();
	while(ch >= '0' && ch <= '9') x = x*10+ch-'0', ch = getchar();
	return x;
}

const int maxn = 1e5+5, maxa = 105;
int N, Q, a[maxn], b[maxn];
double dp[maxn][maxa], ans;

int main() {
	N = read();
	for(int i = 1; i <= N; ++i) a[i] = b[i] = read(), dp[i][b[i]] = 1;
	
	Q = read();
	for(int i = 1; i <= N; ++i) ans += dp[i][0];
	while(Q--) {
		int x = read(), y = read(), k = read();
		ans -= dp[x][0];
		for(int i = 1; i <= k; ++i) {
			for(int j = 1; j <= b[x]; ++j) {
				dp[x][j-1] += 1.0*j/a[x] * dp[x][j];
				dp[x][j] *= 1.0*(a[x]-j)/a[x];
			}
			--a[x];
		}
		a[y] += k;
		ans += dp[x][0];
		printf("%.10lf\n", ans);
	}
	return 0;
}
