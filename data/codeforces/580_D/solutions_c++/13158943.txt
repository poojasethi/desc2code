#include <cstdio>
#include <cstring>
#include <iostream>
int n, m, k, a[30], increase[30][30];
long long dp[22][1<<20];

long long solve(int x, int pre, int st)
{
	if(x == m) return 0;
	if(dp[pre][st] != -1) return dp[pre][st];
	long long &res = dp[pre][st]; res = 0;
	for(int i = 0; i < n; i++)
	{
		if(st & (1 << i)) continue;
		res = std::max(res, solve(x + 1, i, st | (1 << i)) + a[i] + increase[pre][i]);
	}
	return res;
}

int main()
{
	scanf("%d%d%d", &n, &m, &k);
	for(int i = 0; i < n; i++) scanf("%d", &a[i]);
	for(int i = 0; i < k; i++)
	{
		int x, y, c; scanf("%d%d%d", &x, &y, &c);
		increase[x-1][y-1] = c;
	}
	memset(dp, -1, sizeof(dp));
	std::cout << solve(0, n+1, 0) << std::endl;
	return 0;
}
