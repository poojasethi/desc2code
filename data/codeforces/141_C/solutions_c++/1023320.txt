#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  int N;
  cin >> N;
  vector<pair<int,string> > v(N);
  for (int i = 0; i < N; i++) {
    cin >> v[i].second >> v[i].first;
  }
  sort(v.begin(), v.end());
  vector<int> ans(N, 0);
  for (int i = 0; i < N; i++) {
    const int a = v[i].first;
    int r = i-a;
    if (r < 0) {
      cout << -1 << endl;
      return 0;
    }
    for (int j = 0; j < i; j++) {
      if (ans[j] >= r) {
        ++ans[j];
      }
    }
    ans[i] = r;
  }
  for (int i = 0; i < N; i++) {
    cout << v[i].second << ' ' << ans[i]+1 << endl;
  }
  return 0;
}
