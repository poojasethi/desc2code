#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
const int MAX_N = 1e5+7;
vector<int> G[MAX_N];
int nodes;
int pos[MAX_N], ans[MAX_N];
vector<int> com[MAX_N];
int tm;
int start[MAX_N], end[MAX_N];
int dfs(int x, int p)
{
  ++tm;
  start[x] = tm;
  pos[tm] = x;
  for (int i = 0; i < G[x].size(); i++) if (G[x][i] != p)
    dfs(G[x][i], x);
  end[x] = tm;
}

int segTree[3*MAX_N];
int zero[3*MAX_N];

void upd(int node, int beg, int end)
{
  if (segTree[node])
    zero[node] = end-beg+1;
  else if (beg != end)
    zero[node] = zero[2*node]+zero[2*node+1];
  else
    zero[node] = 0;
}

void updateTree(int node, int beg, int end, int from, int to, int v)
{
  if (beg > end || beg > to || end < from)
    ;
  else if (beg >= from && end <= to)
    segTree[node] += v;
  else
    updateTree(2*node, beg, (beg+end)/2, from, to, v), updateTree(2*node+1, (beg+end)/2 + 1, end, from, to, v);
  upd(node, beg, end);
}

void DFS(int x, int p)
{
  for (int i = 0; i < com[x].size(); i++) {
    int y = com[x][i];
    updateTree(1, 1, nodes, start[x], end[x], 1);
    updateTree(1, 1, nodes, start[y], end[y], 1);
  }
  ans[x] = zero[1];
  for (int i = 0; i < G[x].size(); i++) if (G[x][i] != p)
    DFS(G[x][i], x);

  for (int i = 0; i < com[x].size(); i++) {
    int y = com[x][i];
    updateTree(1, 1, nodes, start[x], end[x], -1);
    updateTree(1, 1, nodes, start[y], end[y], -1);
  }
}
int main()
{
//  freopen("in.in", "r", stdin);
  int m;
  cin>>nodes>>m;
  for (int i = 1; i <= nodes -1; i++) {
    int a, b;
    cin>>a>>b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  dfs(1, -1);
  for (int i = 1; i <= m; i++) {
    int a, b;
    cin>>a>>b;
    com[a].push_back(b);
    com[b].push_back(a);    
  }
  DFS(1, -1);
  for (int i = 1; i <= nodes; i++)
    cout<<max(0, ans[i]-1)<<endl;
  return 0;
}