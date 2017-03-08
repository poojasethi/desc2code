#include<iostream>
#include<string>
using namespace std;
const int MAX_N = 1e5+7;
int n, k;
char wall[2][MAX_N];
bool vis[2][MAX_N];
bool ok;
void dfs(bool l, int h, int t)
{
  if (h > n || h + k > n) {
    ok = true;
    return;
  }
  vis[l][h] = true;
  if (wall[!l][h+k] != 'X' && !vis[!l][h+k])
    dfs(!l, h+k, t+1);
  if (wall[l][h+1] != 'X' && !vis[l][h+1])
    dfs(l, h+1, t+1);
  if (h-1 > t+1 && wall[l][h-1] != 'X' && !vis[l][h-1])
    dfs(l, h-1, t+1);
}
int main()
{
  cin>>n>>k;
  cin>>wall[0]+1>>wall[1]+1;
  dfs(0,1,0);
  if (ok) cout<<"YES"<<endl;
  else cout<<"NO"<<endl;
  return 0;
}
