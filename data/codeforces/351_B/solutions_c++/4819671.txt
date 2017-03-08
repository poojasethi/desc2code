#include <iostream>
using namespace std;
int main() {
  int n;
  cin >> n;
  int p[3000];
  int inv = 0;
  for(int i = 0; i < n; i++) {
    cin >> p[i];
    for(int j = 0; j < i; j++) {
      if(p[j] > p[i])
        inv++;
    }
  }
  if(inv % 2)
    cout << 2 * inv - 1 << endl;
  else
    cout << 2 * inv << endl;
}