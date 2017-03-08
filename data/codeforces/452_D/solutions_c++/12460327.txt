#include <stdio.h>
#define max(a,b) ((a)>(b)?(a):(b))
int dp[10001];
int main()
{
	int i,k,n1,n2,n3,t1,t2,t3;
	scanf("%d%d%d%d%d%d%d",&k,&n1,&n2,&n3,&t1,&t2,&t3);
	for (i=1;i<=k;i++)
	{
		dp[i]=t1+t2+t3;
		if (i>=n1)
			dp[i]=max(dp[i],dp[i-n1]+t1);
		if (i>=n2)
			dp[i]=max(dp[i],dp[i-n2]+t2);
		if (i>=n3)
			dp[i]=max(dp[i],dp[i-n3]+t3);
	}
	printf("%d",dp[k]);
	return 0;
}
