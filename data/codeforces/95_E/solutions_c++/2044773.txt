#include<iostream>
#include<algorithm>
using namespace std;
const int oo = int(1e7);
const int MAX_N = 100010;
int parent[MAX_N];
int find(int x)
{
  return (x==parent[x])?x:parent[x] = find(parent[x]);
}
bool islucky(int x)
{
  while (x) { if (x%10 != 7 && x%10 != 4) return false; x /= 10; }
  return true;
}
int n, m, sz[MAX_N], cnt[MAX_N], dp[MAX_N];
int main()
{
  cin>>n>>m;
  for (int i = 1; i <= n; i++) parent[i] = i;
  for (int i = 1; i <= m; i++) {
    int a, b;
    cin>>a>>b;
    parent[find(a)] = find(b);
  }
  for (int i = 1; i <= n; i++) ++sz[find(i)];
  for (int i = 1; i <= n; i++) ++cnt[sz[i]];
  fill(dp+1, dp+n+1, oo);
  dp[0] = 0;
  for (int i = 1; i <= n; i++) if (cnt[i] > 0) {
      for (int b = 1, x = cnt[i]; x > 0; b <<= 1) {
	int c = min(b, x);
	x -= b;
	int k = i*c;
	for (int j = n - k; j >= 0; j--)
	  dp[j+k] = min(dp[j+k], dp[j]+c);
      }
    }
  int ans = oo;
  for (int i = 1; i <= n; i++) if (islucky(i)) ans = min(ans, dp[i]);
  if (ans == oo)
    cout<<"-1"<<endl;
  else
    cout<<ans-1<<endl;
  return 0;
}
