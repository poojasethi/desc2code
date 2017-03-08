#include<iostream>
#include<vector>
using namespace std;
const int MAX_N = int(1e6)+7;
vector<int> G[MAX_N];
int n, m, k;
bool vis[MAX_N];
int dfs(int x)
{
  vis[x] = true;
  int ret = 1;
  for (int i = 0; i < G[x].size(); i++) if (!vis[G[x][i]]) ret += dfs(G[x][i]);
  return ret;
}
int main()
{
  cin>>n>>m>>k;
  for (int i = 0; i < m; i++) {
    int a, b;
    cin>>a>>b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  int sum = 0, comp = 0;
  for (int i = 1; i <= n; i++) if (!vis[i]) sum += min(k, dfs(i)), comp++;
  int ans = max(0, comp - sum/2 - 1);
  if (k == 1) ans = max(0,comp - 2);
  cout<<ans<<endl;
  return 0;
}
