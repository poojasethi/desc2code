#include<bits/stdc++.h>
using namespace std;
const int nmax=5009;
const int mod=1e9+7;
int n,a,b,k;
long long dp[nmax][nmax];
int main(){
   cin>>n>>a>>b>>k;
   for(int i=a;i<=n;i++){
      dp[0][i]=1;
   }
   for(int i=1;i<=k;i++){
      for(int j=1;j<=n;j++){
         if(j<b)
            dp[i][j]=(dp[i-1][(j+b-1)/2]-dp[i-1][0]-dp[i-1][j]+dp[i-1][j-1])%mod;
         if(j>b)
            dp[i][j]=(dp[i-1][n]-dp[i-1][(j+b)/2]-dp[i-1][j]+dp[i-1][j-1])%mod;
      }
      for(int j=1;j<=n;j++){
         dp[i][j]+=dp[i][j-1];
      }
   }
   cout<<(dp[k][n]+mod)%mod<<"\n";
}
