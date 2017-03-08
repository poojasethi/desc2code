#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
long long countFirst(long long n)
{
  long long ret = 0;
  for (long long i = 1; i <= n && i > 0; i *= 10) {
    ret += min(i, n-i+1);
  }
  return ret;
}
long double dp[1024][1024];
long long l[1024], r[1024];
int main()
{
  int n;
  int k;
  cin>>n;
  for (int i = 1; i <= n; i++) cin>>l[i]>>r[i];
  cin>>k;
  dp[0][0] = 1;
  for (int i = 1; i <= n; i++)
    for (int j = 0; j < n; j++) {
      dp[i][j+1] += dp[i-1][j]*(countFirst(r[i]) - countFirst(l[i]-1))/(long double)(r[i] - l[i] + 1);
      dp[i][j] += dp[i-1][j]*(1.0 - (countFirst(r[i]) - countFirst(l[i]-1))/(long double)(r[i] - l[i] + 1));
    }
  k = ceil(n*k/100.0);
  double ans = 0.0;
  for (int i = k; i <= n; i++) ans += dp[n][i];
  printf ("%.12lf\n", ans);
  return 0;
}
