#include <bits/stdc++.h>

using namespace std;

int n, b[5010];
pair<int,int> a[5010];

bool inter(const pair<int,int>& a, const pair<int,int>& b) {
  return (a.first < b.first && b.first < a.second) || (b.first < a.first && a.first < b.second);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> a[i].first >> a[i].second;

  int sum = 0, ways = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) if (i != j) {
      b[i] += inter(a[i], a[j]);
    }
    sum += b[i];
  }

  vector<int> ans;
  for (int i = 0; i < n; i++) {
    if (sum - b[i] - b[i] == 0) {
      ways++;
      ans.push_back(i+1);
    }
  }

  cout << ways << '\n';
  for (int i = 0; i < ways; i++)
    cout << ans[i] << ' ';

  return 0;
}
