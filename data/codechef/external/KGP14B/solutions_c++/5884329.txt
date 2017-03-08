/* bhupkas */

using namespace std;

#include "bits/stdc++.h"

int dp[1005][1005];

int main()
{
	int t;
	cin >> t;
	int n,m;
	string str1,str2;
	for(int tc = 1 ; tc <= t ; tc++)
	{
		cin >> n >> m;
		cin >> str1;
		cin >> str2;
		for(int i = 0 ; i <= n ; ++i)	for(int j = 0 ; j <= m ; ++j)	dp[i][j] = 1000000000;
		for(int i = 0 ; i <= n ; ++i)	dp[i][0] = i;
		for(int i = 0 ; i <= m ; ++i)	dp[0][i] = i;
		for(int i = 1 ; i <= n ; ++i)
		{
			for(int j = 1 ; j <= m ; ++j)
			{
				if(str1[i-1] == str2[j-1])	dp[i][j] = min(dp[i][j],dp[i-1][j-1] + 1);
				else	dp[i][j] = min(dp[i][j],min(dp[i][j-1],dp[i-1][j]) + 1);
			}
		}
		cout << "Case " << tc << ": " << dp[n][m] << endl;
	}
	return 0;
}