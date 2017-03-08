#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define pii pair<long long, int>
#define mp make_pair
vector<int> G[100001];
bool vis[100001];
int k[100001];
pii dfs(int s)
{
  vis[s] = true;
  vector< pii > munch;
  for (int i = 0; i < G[s].size(); i++) if(!vis[G[s][i]]) {
      k[G[s][i]]--;
      munch.push_back(dfs(G[s][i]));
    }
  sort(munch.begin(), munch.end());
  pii ans = mp(0, 0);
  int extra = 0;
  for (int i = 1; k[s] && i <= munch.size(); i++) {
    ans.first += munch[munch.size()-i].first + 2;
    k[s]--;
    extra += munch[munch.size()-i].second;
  }
  int c = min(extra, k[s]);
  k[s] -= c;
  ans.first += 2*c; ans.second = k[s];
  return ans;  
}
int main()
{
  int n;
  cin>>n;
  for (int i = 1; i <= n; i++) cin>>k[i];
  for (int i = 1; i <= n-1; i++) {
    int u, v;
    cin>>u>>v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  int s;
  cin>>s;
  cout<<dfs(s).first<<endl;
  return 0;
}
