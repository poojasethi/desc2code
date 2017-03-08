#include<iostream>
using namespace std;
const long long mod = 1000000000 + 7;
long long dp[3103][202];
int boards, wi[202], hi[202], id[202];
int n, len;
int main ()
{
  cin>>n>>len;
  for (int i = 1; i <= n; i++) {
    int a, b;
    cin>>a>>b;
    wi[++boards] = a; hi[boards] = b; id[boards] = i;
    if (a != b) {
      wi[++boards] = b; hi[boards] = a; id[boards] = i;
    }
  }
  for (int b = 1; b <= boards; b++)
    dp[hi[b]][b] = 1;

  for (int l = 1; l <= len; l++)
    for (int i = 1; i <= boards; i++)
      for (int b = 1; b <= boards; b++)
	if (id[b] != id[i] && wi[i] == hi[b])
	  dp[l + hi[b]][b] = (dp[l + hi[b]][b] + dp[l][i])%mod;
  long long ans = 0;
  for (int b = 1; b <= boards; b++) ans = (ans + dp[len][b])%mod;
  cout<<ans<<endl;
  return 0;
}
