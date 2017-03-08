#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
#define pii pair<int,int>
long long dp[51][101][51];
pii p[51][101][51];
struct task
{
  long long a, b;
  int c, id;
  bool operator<(task x) const 
  {
    return c < x.c;
  }
} t[101];
int n, m, k;
void printResults(pii pos, int n)
{
  if (!n) return;
  int i = pos.first, j = pos.second;
  printResults(p[i][j][n], n-1);
  cout<<t[i].id<<" "<<t[i].a + j<<endl;
}
int main()
{
  memset(dp, -1, sizeof(dp));
  cin>>n>>m>>k;
  for (int i = 1; i <= m; i++)
    cin>>t[i].a>>t[i].b>>t[i].c, t[i].id = i;
  sort (t + 1, t + m + 1);

  for (int i = 1; i <= m; i++)
    for (int j = 0; j <= (t[i].b - t[i].a); j++) {
      dp[i][j][1] = t[i].a + j;
      for (int s = 2; s <= min(n, i); s++)
	for (int l = i - 1; l >= s-1; l--) if (t[i].c > t[l].c) {
	  bool ok = false;
	  long long nj = (t[i].a + j - k);
	  if (nj >= t[l].a && nj <= t[l].b) ok = true;

	  if (ok && ~dp[l][nj-t[l].a][s-1]) {
	    if (dp[i][j][s] < dp[l][nj-t[l].a][s-1] + dp[i][j][1]) {
	      dp[i][j][s] = dp[l][nj-t[l].a][s-1] + dp[i][j][1];
	      p[i][j][s] = make_pair(l, nj-t[l].a);
	    }	      
	  }
	  ok = false;
	  nj = t[i].a + j;
	  if ((nj%k == 0) && (nj/k >= t[l].a && nj/k <= t[l].b)) ok = true;
	  if (ok && ~dp[l][nj/k - t[l].a][s-1]) {
	    if (dp[i][j][s] < dp[l][nj/k-t[l].a][s-1] + dp[i][j][1]) {
	      dp[i][j][s] = dp[l][nj/k-t[l].a][s-1] + dp[i][j][1];
	      p[i][j][s] = make_pair(l, nj/k-t[l].a);
	    }	      
	  }
	}
    }
  long long ans = -1;
  pii end;
  for (int i = 1; i <= m; i++)
    for (int j = 0; j <= 100; j++)
      if (ans < dp[i][j][n]) ans = dp[i][j][n], end = make_pair(i, j);
  if (ans == -1)
    cout<<"NO"<<endl;
  else {
    cout<<"YES"<<endl;
    printResults(end, n);
  }
  return 0;
}
