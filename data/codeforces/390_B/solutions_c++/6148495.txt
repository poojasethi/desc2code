#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;

  vector<int> a(n, 0);
  for (int i = 0; i < n; i++)
    cin >> a[i];

  long long joy = 0;
  long long b;
  for (int i = 0; i < n; i++) {
    cin >> b;
    if ((a[i]<<1) < b || b < 2)
      joy--;
    else {
      long long t = b/2;
      joy += t*(b-t);
    }
  }

  cout << joy << endl;

  return 0;
}
