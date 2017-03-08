#include <bits/stdc++.h>

using namespace std;

vector< pair<string, int> > A[10001];
bool comp( pair<string, int> a, pair<string, int> b) {
  return a.second>b.second;
}

int main()
{
  int n, m, r;
  pair<string, int> p;
  scanf("%d%d", &n, &m);
  for( int i = 0; i < n; i++ ) {
    cin >> p.first;
    scanf("%d%d",&r , &p.second);
    A[r].push_back(p);
  }
  for( int i = 1; i <= m; i++ ) {
    sort(A[i].begin(), A[i].end(), comp);
    if( A[i].size() > 2 && A[i][2].second == A[i][1].second ) puts("?");
    else cout << A[i][0].first << ' ' <<  A[i][1].first << '\n';
  }
}
