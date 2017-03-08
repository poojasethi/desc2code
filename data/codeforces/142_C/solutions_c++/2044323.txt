#include<iostream>
using namespace std;
char T[3][13] = 
  {"xxx..xx...x.",
   ".x.xxxxxx.x.",
   ".x...xx..xxx"};
int n, m;
int ans, free;
char t[11][11], a[11][11];
void dfs(int x, int y, int v)
{
  if (x >= n-1) {
    if (v > ans) {
      ans = v;
      for (int i = 1; i <= n; i++) for (int j = 1; j <= m; j++) a[i][j] = t[i][j];
    }
    return;
  }
  if (y >= m-1) {
    dfs(x+1, 1, v);
    return;
  }
  if (free/5 + v <= ans) return;
  free -= (t[x][y] == '.');
  for (int i = 0; i < 12; i += 3) {
    bool ok = true;
    for (int r = 0; r < 3; r++)
      for (int c = 0; c < 3; c++)
	if (t[x+r][y+c] != '.' && T[r][i+c] == 'x') ok = false;
    if (ok) {
      for (int r = 0; r < 3; r++)
	for (int c = 0; c < 3; c++)
	  if (T[r][i+c] == 'x') t[x+r][y+c] = 'A'+v;
      free -= 5;
      dfs(x, y+1, v+1);
      for (int r = 0; r < 3; r++)
	for (int c = 0; c < 3; c++)
	  if (T[r][i+c] == 'x') t[x+r][y+c] = '.';
      free += 5;
    }
  }
  dfs(x,y+1,v);
  free += (t[x][y] == '.');
}
int main()
{
  cin>>n>>m;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) t[i][j] = a[i][j] = '.', ++free;
  dfs(1,1,0);
  cout<<ans<<endl;
  for (int i = 1; i <= n; i++) cout<<a[i]+1<<endl;
  return 0;
}
