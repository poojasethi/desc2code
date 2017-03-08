#include <stdio.h>
int n,ww[5001],hh[5001],dp[5001],go[5001];
int dfs(int k)
{
	if (dp[k])
		return dp[k];
	int i,mx=0,t;
	for (i=1;i<=n;i++)
		if (ww[i]>ww[k]&&hh[i]>hh[k])
		{
			t=dfs(i);
			if (t>mx)
			{
				mx=t;
				go[k]=i;
			}
		}
	return dp[k]=mx+1;
}
int main()
{
	int i;
	scanf("%d%d%d",&n,ww,hh);
	for (i=1;i<=n;i++)
		scanf("%d%d",ww+i,hh+i);
	int res=dfs(0);
	printf("%d\n",res-1);
	for (i=0;go[i];)
	{
		printf("%d ",go[i]);
		i=go[i];
	}
	return 0;
}
