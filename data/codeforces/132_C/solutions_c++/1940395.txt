#include<iostream>
#include<string>
#include<cmath>
using namespace std;

bool vis[110][55][2][220];
int ans;
int n, m;
string P;
void solve(int i, int c, int o, int d)
{
  if (vis[i][c][o][d]) return;
  vis[i][c][o][d] = true;
  if (i > n || c > m) return;
  if (i == n && c == m) ans = max(ans, (int)abs(d));
  solve(i + 1, c + (P[i] == 'T'), o, d + ((o==2)?1:-1));
  solve(i + 1, c + (P[i] == 'F'), (o==2)?1:2, d);
  solve(i, c + 2, o, d);
}
int main()
{
  cin>>P;
  n = P.size();
  cin>>m;
  solve(0, 0, 2, 0);
  cout<<ans<<endl;
  return 0;
}
