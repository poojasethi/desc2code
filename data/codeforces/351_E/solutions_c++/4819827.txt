#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int n;
  cin >> n;
  int a[2000];
  for(int i = 0; i < n; i++) {
    cin >> a[i];
    a[i] = abs(a[i]);
  }
  int ans = 0;
  for(int i = 0; i < n; i++) {
    int before = 0, after = 0;
    for(int j = 0; j < i; j++)
      if(a[j] < a[i])
        before++;
    for(int j = i+1; j < n; j++)
      if(a[j] < a[i])
        after++;
    ans += min(before, after);
  }
  cout << ans << endl;
}