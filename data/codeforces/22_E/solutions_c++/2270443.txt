#include<iostream>
#include<vector>
using namespace std;
const int MAX_N = 2e5+7;
int in[MAX_N];
int G[MAX_N];
struct comp
{
  int start, end;
};
vector< comp > c;
bool vis[MAX_N];
int dfs(int x)
{
  while (!vis[x]) vis[x] = 1, x = G[x];
  return x;
}
int main()
{
  int n;
  cin>>n;
  for (int i = 1; i <= n; i++) {
    int f; cin>>f;
    G[i] = f;
    in[f]++;
  }
  for (int i = 1; i <= n; i++) if (!in[i]) {
      comp x = {i, dfs(i)};
      c.push_back(x);
    }
  for (int i = 1; i <= n; i++) if (!vis[i]) {
      comp x = {i, dfs(i)};
      c.push_back(x);
    }
  if (c.size() == 1 && c[0].start == c[0].end)
    cout<<"0"<<endl;
  else {
    cout<<c.size()<<endl;
    for (int i = 0; i < c.size(); i++) {
      int j = (i+1)%c.size();
      cout<<c[i].end<<" "<<c[j].start<<endl;
    }
  }
  return 0;
}
