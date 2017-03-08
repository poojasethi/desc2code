#include<iostream>
#include<vector>
using namespace std;
const int MAX_N = 1e5+7;
vector<int> G[MAX_N];
int tim[MAX_N], low[MAX_N], timer;
bool vis[MAX_N], bridge;
void dfs(int x, int par)
{
  vis[x] = true;
  tim[x] = low[x] = ++timer;
  int children = 0;
  for (int i = 0; i < G[x].size(); i++) if (G[x][i] != par) {
      int to = G[x][i];
      if (!vis[to]) {
	children++;
	dfs(to, x);
	low[x] = min(low[x], low[to]);
	if (low[to] > tim[x]) bridge = true;
      } else {
	low[x] = min(low[x], tim[to]);
      }
    }
}
bool vis2[MAX_N];
void dfs2(int x, int par)
{
  vis2[x] = true;
  tim[x] = ++timer;
  for (int i = 0; i < G[x].size(); i++) {
    int to = G[x][i];
    if (to == par) continue;
    if (tim[to] > tim[x]) continue;
    cout<<x<<" "<<to<<endl;
    if (!vis2[to])
      dfs2(to, x);
  }
}
int main()
{
  int n, m;
  cin>>n>>m;
  for (int i = 0; i < m; i++) {
    int a, b;
    cin>>a>>b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  dfs(1, -1);
  if (bridge)
    cout<<"0"<<endl;
  else {
    dfs2(1, -1);
  }
  return 0;
}
