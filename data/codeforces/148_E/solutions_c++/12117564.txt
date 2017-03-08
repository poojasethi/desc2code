#include <stdio.h>
#include <string.h>
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
int val[101],s[101],dp[10001];
int main()
{
	int n,m,i,j,k,l;
	scanf("%d%d",&n,&m);
	for (i=1;i<=n;i++)
	{
		scanf("%d",&l);
		for (j=1;j<=l;j++)
		{
			scanf("%d",val+j);
			val[j]+=val[j-1];
		}
		memset(s,0,sizeof(s));
		for (j=0;j<l;j++)
			for (k=j;k<=l;k++)
				s[l-k+j]=max(s[l-k+j],val[l]-val[k]+val[j]);
		for (j=m;j>=1;j--)
			for (k=min(j,l);k>=1;k--)
				dp[j]=max(dp[j],dp[j-k]+s[k]);
	}
	printf("%d",dp[m]);
	return 0;
}
