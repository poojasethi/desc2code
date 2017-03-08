#include <bits/stdc++.h>

using namespace std;

string ans;
map< vector<string>, int> seen;

void solve(vector<string> a) {
  if(seen[a]) return;
  seen[a] = 1;

  int n = a.size();
  if(n == 1) {
    ans = "YES";
    return;
  }

  if(n > 1 && (a[n-1][0] == a[n-2][0] || a[n-1][1] == a[n-2][1])) {
    vector<string> b = a;
    b[n-2] = b[n-1];
    b.pop_back();
    solve(b);
  }
  if(n > 3 && (a[n-1][0] == a[n-4][0] || a[n-1][1] == a[n-4][1])) {
    vector<string> b = a;
    b[n-4] = b[n-1];
    b.pop_back();
    solve(b);
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  int n;
  cin >> n;

  vector<string> deck(n);

  for(int i = 0; i < n; i++)
    cin >> deck[i];

  ans = "NO";
  solve(deck);
  cout << ans << endl;
  return 0;
}

