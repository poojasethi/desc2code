#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
const int MAX_N = 3030;
vector<int> G[MAX_N];
vector<int> C[MAX_N];
int s, t;
void dfs(int x, int p, int c)
{
  t = max(t, c);
  for (int i = 0; i < G[x].size(); i++) if (G[x][i] != p) {
      s += C[x][i];
      dfs(G[x][i], x, max(0,c + 2*C[x][i] - 1));
    }
}
int main()
{
  int n;
  cin>>n;
  for (int i = 1; i <= n-1; i++) {
    int a, b;
    cin>>a>>b;
    G[a].push_back(b), C[a].push_back(0);
    G[b].push_back(a), C[b].push_back(1);
  }
  int ans = n;
  for (int i = 1; i <= n; i++) {
    s = 0, t = 0;
    dfs(i, 0, 0);
    ans = min(ans, s-t);
  }
  cout<<ans<<endl;
  return 0;
}
