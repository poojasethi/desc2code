#include <stdio.h>
#include <math.h>
#include <algorithm>
#define mod 1000000007
using namespace std;
long long dp[5001],qzh[5001];
int main()
{
	int n,a,b,k,i,l,r;
	scanf("%d%d%d%d",&n,&a,&b,&k);
	for (i=1;i<=n;i++)
		dp[i]=1;
	while (k--)
	{
		for (i=1;i<=n;i++)
			qzh[i]=(qzh[i-1]+dp[i])%mod;
		for (i=1;i<=n;i++)
		{
			l=max(i-(abs(b-i)-1),1);
			r=min(i+(abs(b-i)-1),n);
			dp[i]=qzh[r]-qzh[l-1]-dp[i]+mod;
		}
	}
	((dp[a]%=mod)+=mod)%=mod;
	printf("%d",dp[a]);
	return 0;
}
