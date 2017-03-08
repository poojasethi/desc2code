# include <stdio.h>
# include <iostream>
# include <algorithm>
# include <limits.h>

# define mi(x,y) (x<y ? x : y)
# define INF INT_MAX
# define MAXN 5009

int dp[MAXN][MAXN], n, D[MAXN], tp, pos[MAXN], ans = INF, fr, a, b;

int main()
{
	scanf("%d",&n);
	
	for(int h=0; h<n; h++)	scanf("%d",&D[h]), pos[D[h]] = h;
	
	for(int h=n-2; h>-1; h--)
	{
		for(int j=1; j<n; j++)
			dp[h][j] = dp[h][j-1] + (D[j-1] > h);
		tp += dp[h][pos[h]];
	}
	
	for(int h=0; h<n; h++)
		for(int j=h+1; j<n; j++)
		{
			a = D[h]; b = D[j];
			int k = tp - dp[a][h] - dp[b][j] + dp[a][j] + dp[b][h] + (a < b) - 
			(j-h-1 - (dp[a][j]-dp[a][h+1])) + (j-h-1 - (dp[b][j]-dp[b][h+1]));
			
			if(ans > k)	ans = k, fr = 1;
			else if(ans == k)	fr++;
		}
	
	printf("%d %d\n",ans,fr);
}
