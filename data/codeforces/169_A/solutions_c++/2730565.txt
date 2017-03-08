#include <iostream>
#include <algorithm>

using namespace std;

int h[2000];

int main() {
  int n, a, b;
  cin >> n >> a >> b;

  for (int i = 0; i < n; i++) {
    cin >> h[i];
  }
  sort(h, h+n);

  cout << h[b] - h[b-1] << endl;
}
