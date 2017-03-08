#include<iostream>
using namespace std;
int a[1501][1501], s[1501][1501];
long long dp[1501][1501];
int n, m;
long long f[1501], b[1501];
int main()
{
  cin>>n>>m;
  for (int i = 1; i <= n; i++) for (int j = 1; j <= m; j++) {
      cin>>a[i][j];
      s[i][j] = a[i][j] + s[i][j-1];
    }
  for (int j = 1; j <= m; j++) dp[1][j] = s[1][j];
  for (int i = 2; i <= n; i++) {
    f[1] = dp[i-1][1];
    for (int j = 2; j <= m; j++) f[j] = max(f[j-1], dp[i-1][j]);
    b[m] = dp[i-1][m];
    for (int j = m-1; j >= 1; j--) b[j] = max(b[j+1], dp[i-1][j]);
    if (i&1) {
      for (int j = 2; j <= m; j++) {
	dp[i][j] = f[j-1] + s[i][j];
      }
    } else {
      for (int j = 1; j <= m-1; j++) {
	dp[i][j] = b[j+1] + s[i][j];
      }
    }
  }
  long long ans;
  if (n&1) {
    ans = dp[n][2];
    for (int j = 2; j <= m; j++) ans = max(ans, dp[n][j]);
  } else {
    ans = dp[n][1];
    for (int j = 1; j <= m-1; j++) ans = max(ans, dp[n][j]);
  }
  cout<<ans<<endl;
  return 0;
}
