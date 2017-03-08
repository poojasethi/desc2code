#include<bits/stdc++.h>
using namespace std;
int dp[2][1002];
char ch[1002][1002];
int cntw[1002],cntb[1002];
int main()
{
    int i,j,n,m,x,y;
    cin>>n>>m>>x>>y;
    for(i=1;i<=n;i++) scanf("%s",ch[i]+1);
    for(j=1;j<=m;j++){
        int s=0;
        for(i=1;i<=n;i++)
            s+=(ch[i][j]=='.');
        cntw[j]=cntw[j-1]+s;
        cntb[j]=cntb[j-1]+n-s;
    }
    memset(dp,0x3f,sizeof dp);
    dp[0][0]=dp[1][0]=0;
    for(j=1;j<=m;j++){
        for(int a=x;a<=y;a++)if(j-a>=0){
            dp[0][j]=min(dp[0][j],dp[1][j-a]+(cntw[j]-cntw[j-a]));
            dp[1][j]=min(dp[1][j],dp[0][j-a]+(cntb[j]-cntb[j-a]));
        }
    }
    cout<<min(dp[0][m],dp[1][m])<<endl;
}
