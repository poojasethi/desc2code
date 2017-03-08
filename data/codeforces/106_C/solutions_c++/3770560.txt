#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int dp[1010][50];
int n,m,a[20],b[20],c[20],d[20],d0,c0;
int main(){
 cin >> n >> m >> c0 >> d0;
 for(int i=1;i<=m;i++)
  scanf("%d %d %d %d",&a[i],&b[i],&c[i],&d[i]);
 for(int i=0;i<=n;i++)
  dp[i][0] = d0*(i/c0);
 for(int i=1;i<=m;i++){
  for(int j=0;j<=n;j++)
   for(int k=0;k<=j;k+=c[i])
    { if((k/c[i])*b[i]>a[i])break;
      dp[j][i] = max(dp[j][i],dp[j-k][i-1]+d[i]*(k/c[i]));
    }
 
 }
cout << dp[n][m] << endl;
 return 0;
}