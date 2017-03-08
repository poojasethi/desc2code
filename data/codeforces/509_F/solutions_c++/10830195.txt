#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
const int MOD=1000000007;
const int MAX=505;
int b[MAX];
LL dp[MAX][MAX];
LL dfs(int l,int r)
{
    if(dp[l][r]>=0)
        return dp[l][r];
    if(l==r)
        return dp[l][r]=1;
    dp[l][r]=dfs(l+1,r);
    for(int i=r-1;i>l;i--)
        if(b[l+1]<b[i+1])
            dp[l][r]=(dp[l][r]+dfs(l+1,i)*dfs(i,r))%MOD;
    return dp[l][r];
}
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        for(int i=1;i<=n;i++)
            scanf("%d",&b[i]);
        memset(dp,-1,sizeof(dp));
        printf("%I64d\n",dfs(1,n));
    }
    return 0;
}
