#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
const int MAX_N = 128;
int xx[MAX_N][MAX_N][MAX_N], yy[MAX_N][MAX_N][MAX_N];
vector<int> ans;
int W, H;
void dfs(int x1, int x2, int y1, int y2)
{
  for (int y = y1+1; y < y2; y++) if (yy[x1][x2][y]) {
    dfs(x1, x2, y, y2);
    dfs(x1, x2, y1, y);
    return;
  }
  for (int x = x1+1; x < x2; x++) if (xx[y1][y2][x]) {
    dfs(x1, x, y1, y2);
    dfs(x, x2, y1, y2);
    return;
  }
  ans.push_back(abs(y1-y2)*abs(x1-x2));
}
int main()
{
  int n;
  cin>>W>>H>>n;
  for (int i = 0; i < n; i++) {
    int x1, x2, y1, y2;
    cin>>x1>>y1>>x2>>y2;
    if (x1 > x2) swap(x1, x2);
    if (y1 > y2) swap(y1, y2);
    if (x1 == x2) xx[y1][y2][x1] = 1;
    if (y1 == y2) yy[x1][x2][y1] = 1;
  }
  dfs(0, W, 0, H);
  sort(ans.begin(), ans.end());
  for (int i = 0; i < ans.size(); i++) cout<<ans[i]<<" ";cout<<endl;
}
