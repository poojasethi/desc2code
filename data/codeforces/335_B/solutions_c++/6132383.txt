#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  string s;
  cin >> s;

  int n = s.size();

  vector< vector<int> > A(2, vector<int>());

  vector<int> C(n, 0);
  vector<int> B(n, 1);
  //for (int i = 0; i < n; i++) 
    //A[i][i+1] = 1;
  int i0 = 0, j0 = 1;
  int l = 1;

  int k, i;
  bool bflag = true;
  for (k = 2; bflag && k <= n; k++) {
    vector<int> CC(B);
    vector<int> v;
    for (i = 0; bflag && i <= n-k; i++) {
      v.push_back(2);
      if (B[i+1] > B[i]) {
        B[i] = B[i+1];
        v[i] = 1;
      }
      if (s[i]==s[i+k-1] && C[i+1]+2>B[i]) {
        B[i] = C[i+1]+2;
        v[i] = 3;
      }

      if (B[i] > l) {
        l = B[i];
        i0 = i;
        j0 = i+k;
      }
      if (B[i] >= 100)
        bflag = false;
    }
    C = CC;
    A.push_back(v);
  }

  int m = min(l, 100);
  string t(m, ' ');
  if (i0+1 == j0) {
    t[0] = s[i0];
  }
  else {
    int l = 0;
    int r = m-1;
    while (l < r) {
      if (A[j0-i0][i0] == 3) {
        t[l++] = t[r--] = s[i0];
        i0++;
        j0--;
      }
      else if (A[j0-i0][i0] == 2)
        j0--;
      else
        i0++;
    }
    if (l == r)
      t[l] = s[i0];
  }
  cout << t << endl;

  return 0;
}
