#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int w[100005];

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> wq;
  for(int i = 0; i < m; i++) {
    int q;
    cin >> q >> w[i];
  }
  sort(w, w + m, greater<int>());
  int i = 0;
  while(i * (i/2) + (i%2) <= n) i++;
  i--;
  // cout << i << endl;
  long long ans = 0;
  for(int j = 0; j < i; j++)
    ans += w[j];
  cout << ans << endl;
}