#include<iostream>
#include<vector>
using namespace std;
const int MAX_N = 1e5+7;
typedef long long ll;
const ll mod = 1e9+7;
vector<int> G[MAX_N], T[MAX_N];
int cycle[MAX_N];
bool incycle[MAX_N];
int n, m;
int vis[MAX_N], father[MAX_N];
int find_cycles(int x, int par)
{
  vis[x] = 1;
  father[x] = par;
  for (int y = 0; y < G[x].size(); y++) if (G[x][y] != par) {
      if (!vis[G[x][y]])
	cycle[x] += find_cycles(G[x][y], x);
      else if (vis[G[x][y]] == 1) 
	cycle[x] = G[x][y];
    }
  vis[x] = 2;
  if (cycle[x]) incycle[x] = true;
  return (cycle[x]==x)?0:cycle[x];
}
int deg[MAX_N];
void dfs(int x, int d, int par)
{
  vis[x] = true;
  d += incycle[x];
  deg[x] = d;
  for (int y = 0; y < T[x].size(); y++) if (!vis[T[x][y]]) {
      dfs(T[x][y], d, x);
    }
}
int ancestor[MAX_N][20], logN;
int start[MAX_N], end[MAX_N], timer;
void lca_init(int x, int par = 0)
{
  start[x] = ++timer;
  vis[x] = true;
  ancestor[x][0] = par;
  for (int i = 1; i <= logN; i++)
    ancestor[x][i] = ancestor[ancestor[x][i-1]][i-1];
  for (int y = 0; y < T[x].size(); y++) if (T[x][y] != par && !vis[T[x][y]])
    lca_init(T[x][y], x);
  end[x] = ++timer;
}
bool upper(int a, int b)
{
  if (start[a] <= start[b] && end[a] >= end[b]) return true;
  return false;
}
int lca(int a, int b)
{
  if (upper(a,b)) return a;
  if (upper(b,a)) return b;
  for (int i = logN; i >= 0; i--)
    if (ancestor[a][i]&&!upper(ancestor[a][i],b)) a = ancestor[a][i];
  return ancestor[a][0];
}
ll pow2[MAX_N];
int main()
{
  cin>>n>>m;

  pow2[0] = 1;
  for (int i = 1; i <= n; i++) pow2[i] = (2*pow2[i-1])%mod;

  for (int i = 1; i <= m; i++) {
    int a, b;
    cin>>a>>b;
    G[a].push_back(b), G[b].push_back(a);
  }
  find_cycles(1, 0);
  for (int i = 1; i <= n; i++) if (!cycle[i]) cycle[i] = i;
  for (int i = 1; i <= n; i++)
    T[cycle[i]].insert(T[cycle[i]].end(), G[i].begin(), G[i].end());
  for (int i = 1; i <= n; i++) if (cycle[i] == i) {
      for (int j = 0; j < T[i].size(); j++)
	T[i][j] = cycle[T[i][j]];
    }
  for (int i = 1; i <= n; i++) vis[i] = false;
  dfs(cycle[1], 0, -1);
  logN = 0;
  while (1<<logN < n) ++logN;
  for (int i = 1; i <= n; i++) vis[i] = false;
  lca_init(cycle[1]);
  int k;
  cin>>k;
  for (int i = 0; i < k; i++) {
    int a, b;
    cin>>a>>b;
    a = cycle[a], b = cycle[b];
    int l = lca(a, b);
    if (a == b) cout<<2<<endl;
    else {
      int d = deg[a] + deg[b] - 2*deg[l] + incycle[l];
      cout<<pow2[d]<<endl;
    }
  }
  return 0;
}
