#include<bits/stdc++.h>
using namespace std;
double dp[101][101][101];
double dfs(int i,int j,int k){
    if(!k) return dp[i][j][k]=1;
    if(!(i&&j)) return dp[i][j][k]=0;
    if(dp[i][j][k]) return dp[i][j][k];
    return dp[i][j][k]=(i*j*dfs(i,j-1,k)+k*i*dfs(i-1,j,k)+j*k*dfs(i,j,k-1))/(i*j+j*k+k*i);
}
int main()
{
    int i,j,r,s,p,t;
    cin>>r>>s>>p;
    printf("%.12f ",dfs(r,s,p));
    memset(dp,0,sizeof dp);
    printf("%.12f ",dfs(s,p,r));
    memset(dp,0,sizeof dp);
    printf("%.12f\n",dfs(p,r,s));
}
