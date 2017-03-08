#include<iostream>
#include<vector>
using namespace std;
int m, n, maxk;
vector<int> color[100001];
int main()
{
  cin>>n>>m>>maxk;
  for (int i = 1; i <= n; i++) {
    int c; cin>>c;
    color[c].push_back(i);
  }
  int ans = 0;
  for (int c = 1; c <= m; c++) {
    for (int i = 0, j = 0; j < color[c].size(); j++) {
      while ((color[c][j] - color[c][i]-j+i) > maxk) i++;
      ans = max(ans, j-i+1);
    }
  }
  cout<<ans<<endl;
  return 0;
}
