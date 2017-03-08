#include <stdio.h>
int par[2001];
int fnd(int k)
{
	return par[k]==k?k:par[k]=fnd(par[k]);
}
int main()
{
	int n,m,k,i,j;
	long long ans=1;
	scanf("%d%d%d",&n,&m,&k);
	for (i=1;i<=n;i++)
		par[i]=i;
	for (i=1;i<=n-k+1;i++)
		for (j=1;j<=k/2;j++)
			par[fnd(i+j-1)]=fnd(i+k-j);
	for (i=1;i<=n;i++)
		if (par[i]==i)
			ans=ans*m%1000000007;
	printf("%I64d",ans);
	return 0;
}
