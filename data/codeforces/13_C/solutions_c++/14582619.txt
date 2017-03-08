#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int a[5001],b[5001];
long long dp[5001];
int main()
{
	int n;
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
		scanf("%d",a+i);
	memcpy(b,a,sizeof(a));
	sort(b+1,b+n+1);
	dp[0]=1000000000000000000;
	for (int i=1;i<=n;i++)
        for (int j=1;j<=n;j++)
            dp[j]=min(dp[j]+abs(b[j]-a[i]),dp[j-1]);
    printf("%I64d",dp[n]);
	return 0;
}
