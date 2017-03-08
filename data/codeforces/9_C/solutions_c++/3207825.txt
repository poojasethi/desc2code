#include<stdio.h>
int n,ans=0;
void dfs(int x)
{
	if(x<=n)
	{
		ans++;
		dfs(10*x);
		dfs(10*x+1);
	}
}

int main()
{
	while(scanf("%d",&n)!=EOF)
	{
		dfs(1);
		printf("%d\n",ans);
	}
	return 0;
}