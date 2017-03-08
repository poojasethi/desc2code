#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<queue>
#include<deque>
using namespace std;
typedef long long ll;
class Queue
{
  deque<int> minm;
  queue<int> Q;
public:
  void push(ll x)
  {
    while (!minm.empty() && minm.back() > x) minm.pop_back();
    minm.push_back(x);
    Q.push(x);
  }
  int pop()
  {
    ll ret = Q.front(); Q.pop();
    if (ret == minm.front()) minm.pop_front();
    return ret;
  }
  int min()
  {
    return minm.front();
  }
};
ll mat[1024][1024], accu[1024][1024];
int minh[1024][1024];
bool bad[1024][1024];
int main()
{
  int n, m, a, b;
  scanf ("%d %d %d %d", &n, &m, &a, &b);
  for (int r = 1; r <= n; r++)
    for (int c = 1; c <= m; c++) scanf ("%I64d", &mat[r][c]);

  for (int r = 1; r <= n; r++)
    for (int c = 1; c <= m; c++)
      accu[r][c] = accu[r-1][c]+accu[r][c-1]-accu[r-1][c-1]+mat[r][c];
  for (int c = 1; c <= m; c++) {
    Queue Q;
    for (int r = 1; r <= a; r++) Q.push(mat[r][c]);
    minh[1][c] = Q.min();
    for (int r = a+1; r <= n; r++) {
      Q.pop(); Q.push(mat[r][c]);
      minh[r-a+1][c] = Q.min();
    }
  }
  for (int r = 1; r <= n; r++) {
    Queue Q;
    for (int c = 1; c <= b; c++) Q.push(minh[r][c]);
    minh[r][1] = Q.min();
    for (int c = b+1; c <= m; c++) {
      Q.pop(); Q.push(minh[r][c]);
      minh[r][c-b+1] = Q.min();
    }
  }

  vector< pair<ll, pair<int, int> > > res;
  for (int r = 1; r <= n-a+1; r++)
    for (int c = 1; c <= m-b+1; c++) {
      ll sum = accu[r+a-1][c+b-1]-accu[r-1][c+b-1]-accu[r+a-1][c-1]+accu[r-1][c-1];
      ll x = sum - (long long)minh[r][c]*a*b;
      res.push_back(make_pair(x, make_pair(r,c)));
    }
  sort(res.begin(), res.end());
  vector< pair<ll, pair<int, int> > > ans;
  for (int i = 0; i < res.size(); i++) {
    int r = res[i].second.first, c = res[i].second.second;
    ll x = res[i].first;
    if (bad[r][c] || bad[r][c+b-1] || bad[r+a-1][c] || bad[r+a-1][c+b-1]) continue;
    ans.push_back(make_pair(x,make_pair(r,c)));
    for (int rr = r; rr < r+a; rr++)
      for (int cc = c; cc < c+b; cc++) bad[rr][cc] = true;
  }
  printf ("%d\n", ans.size());
  for (int i = 0; i < ans.size(); i++)
    printf ("%d %d %I64d\n", ans[i].second.first,ans[i].second.second,ans[i].first);
  return 0;
}
