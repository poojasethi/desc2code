#include<iostream>
#include<cstring>
using namespace std;
int dp[42][64][64];
int main()
{
  int n, m;
  cin>>n>>m;
  if (m < n) m^=n,n^=m,m^=n;
  int mask = (1<<n)-1;
  memset(dp, 63, sizeof(dp));
  dp[0][mask][0] = 0;
  for (int i = 1; i <= m + 1; i++)
    for (int x = 0; x <= mask; x++)
      for (int y = 0; y <= mask; y++)
	for (int z = 0; z <= mask; z++) {
	  bool valid[8], ok = true;
	  for (int b = 1; b <= n; b++) valid[b] = false;
	  for (int b = 0; b < n; b++) {
	    if ((1<<b)&x) valid[b+1] = true;
	    if ((1<<b)&y) valid[b+1] = valid[b] = valid[b+2] = true;
	    if ((1<<b)&z) valid[b+1] = true;
	  }
	  for (int b = 1; b <= n; b++) if (!valid[b]) ok = false;
	  if (!ok) continue;
	  dp[i][y][z] = min(dp[i][y][z], dp[i-1][x][y] + __builtin_popcount(z));
	}
  int ans = 0;
  for (int i = 0; i <= mask; i++) ans = max(ans, n*m - dp[m+1][i][0]);
  cout<<ans<<endl;
  return 0;
}
