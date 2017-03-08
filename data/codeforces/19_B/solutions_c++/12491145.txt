#include <stdio.h>
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
int t[2001],c[2001];
long long dp[2001][2001];
int main()
{
	int n,i,j;
	scanf("%d",&n);
	for (i=1;i<=n;i++)
	{
		scanf("%d%d",t+i,c+i);
		t[i]++;
	}
	for (i=1;i<=n;i++)
		dp[0][i]=1000000000000000000;
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++)
			dp[i][j]=min(dp[i-1][j],dp[i-1][max(j-t[i],0)]+c[i]);
	printf("%I64d",dp[n][n]);
	return 0;
}
