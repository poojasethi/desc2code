/* bhupkas */

#include "bits/stdc++.h"

using namespace std;
int dp[4005][4004];
int main()
{
	int n;
	int v[4010];
	cin >> n;
	memset(dp,0,sizeof(dp));
	for(int i = 1 ; i <= n ; i++)	cin >> v[i];
	int ans = -1;
	for(int i = 1 ; i <= n ; i++)
	{
		int prev = 0;
		for(int j = 0 ; j < i ; j++)
		{
			dp[i][j] = dp[j][prev] + 1;
			if(v[i] == v[j])	prev = j;
			ans = max(dp[i][j],ans);
		}
	}
	cout << ans << endl;
	return 0;
}
