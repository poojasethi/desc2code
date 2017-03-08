#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define MAX 1000010
const int mod = 1e9 + 7;
int p[MAX], v[MAX];
long long ways[MAX], s[MAX];
pair<int, int> points[MAX];
int main()
{
  int n, m;
  cin>>n>>m;
  for (int i = 0; i < m; i++)
    cin>>points[i].second>>points[i].first;
  sort(points, points + m);
  int e;
  v[1] = points[0].first; p[0] = e = 1;
  for (int i = 1; i < m; i++) {
    if (points[i].first != points[i - 1].first) v[++e] = points[i].first;
    p[i] = e;
  }
  ways[0] = s[0] = 1;
  for (int i = 0; i < m; i++) {
    int lo = 0, hi = p[i];
    while (lo < hi) {
      int mi = (lo + hi)/2;
      if (v[mi] < points[i].second) lo = mi+1;
      else hi = mi;
    }
    if (hi < p[i])
      ways[p[i]] = (ways[p[i]] + s[p[i] - 1] - (hi?s[hi-1]:0) + mod)%mod;
    if (p[i] != p[i+1])
      s[p[i]] = (s[p[i] - 1] + ways[p[i]] + mod)%mod;
  }
  if (v[e] == n)
    cout<<(ways[e] + mod)%mod<<endl;
  else
    cout<<0<<endl;
  return 0;
}
