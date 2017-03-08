#include <iostream>

using namespace std;

int a[1000];

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  int m = min(a[0], a[n-1]);
  for (int i = 1; i <= n - 3; i++) {
    m = min(m, max(a[i], a[i+1]));
  }

  cout << m << endl;
}
