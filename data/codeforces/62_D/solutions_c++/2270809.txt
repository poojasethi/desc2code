#include<iostream>
using namespace std;
const int MAX_N = 2048;
int ans[MAX_N];
int n, m;
int G[MAX_N][MAX_N];
int seq[MAX_N];
int dfs(int x, int idx, bool gt)
{
  ans[idx] = x;
  if (idx == m+1) return gt;
  for (int i = (gt?1:seq[idx+1]); i <= n; i++) if (G[x][i]) {
      G[x][i]--, G[i][x]--;
      if (dfs(i, idx+1, gt || i > seq[idx+1])) return true;
      G[x][i]++, G[i][x]++;
    }
  return false;
}
int main()
{
  cin>>n>>m;
  for (int i = 1; i <= m+1; i++) {
    cin>>seq[i];
    G[seq[i]][seq[i-1]] = 1;
    G[seq[i-1]][seq[i]] = 1;
  }

  if (dfs(seq[1], 1, 0)) {
    for (int i = 1; i <= m + 1; i++) cout<<ans[i]<<" ";cout<<endl;
  } else cout<<"No solution"<<endl;
  return 0;
}
