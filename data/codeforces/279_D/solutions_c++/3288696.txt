#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 23
#define INF 100
using namespace std;
int memo[1 << MAXN];
int n, a[MAXN];
int dfs(int mask) {
	if(memo[mask] != -1)
		return memo[mask];
	int bits = __builtin_popcount(mask);
	int opt = INF;
	for(int i = n - 1; i >= 0; --i) {
		if(mask & (1 << i)) {
			int nmask = mask ^ (1 << i) | (1 << (i - 1));
			for(int j = 0; j < i; ++j)
				for(int k = 0; k <= j; ++k)
					if(a[j] + a[k] == a[i]) {
						int ans = dfs(nmask | (1 << j) | (1 << k));
						opt = min(opt, max(bits, ans));
					}
			break;
		}
	}	
	return memo[mask] = opt;
}
int main() {
	scanf("%d", &n);
	for(int i = 0; i < n; ++i) {
		scanf("%d", &a[i]);
	}
	memset(memo, -1, sizeof(memo));
	memo[1] = 1;
	int ans = dfs(1 << (n - 1));
	if(ans < INF)
		printf("%d\n", ans);
	else
		printf("-1\n");
	return 0;
}
