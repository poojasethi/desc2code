#include <stdio.h>
int n,m,k,log2[1<<11],g[11][11],used[11],vst[11][11];
int dfs(int x,int y)
{
	if (y>m)
	{
		x++;
		y=1;
	}
	if (x>n)
		return 1;
	int cnt=0,w=-1,cc=vst[x-1][y]|vst[x][y-1],i;
	for (i=(~cc)&((1<<k)-1);i;i-=(i&(-i)))
	{
		int nm=log2[i&(-i)]+1;
		if (!g[x][y]||g[x][y]==nm)
		{
			vst[x][y]=cc|(1<<(nm-1));
			used[nm]++;
			if (used[nm]==1)
			{
				if (w==-1)
					w=dfs(x,y+1);
				cnt+=w;
			}
			else if (used[nm])
				cnt+=dfs(x,y+1);
			cnt%=1000000007;
			used[nm]--;
		}
	}
	return cnt;
}
int main()
{
	int i,j;
	scanf("%d%d%d",&n,&m,&k);
	if (k<n+m-1)
	{
		printf("0");
		return 0;
	}
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++)
		{
			scanf("%d",&g[i][j]);
			used[g[i][j]]++;
		}
	for (i=0;i<=10;i++)
		log2[1<<i]=i;
	printf("%d",dfs(1,1));
	return 0;
}
