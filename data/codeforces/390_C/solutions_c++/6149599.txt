#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  int n, k, w;
  cin >> n >> k >> w;
  string B;
  cin >> B;

  vector<vector<int> > V(k);
  for (int i = 0; i < k; i++) {
    int t = 0;
    V[i].push_back(t);
    for (int j = 0; i+j < n; j++) {
      if (j%k == k-1) {
        if (B[i+j] == '0')
          t++;
        V[i].push_back(t);
      }
      else { 
        if (B[i+j] == '1')
          t++;
      }
    }
  }

  int l, r;
  while (w--) {
    cin >> l >> r;
    l--;
    int i = l%k;
    cout << V[i][r/k]-V[i][l/k] << endl;
  }
  
  return 0;
}
