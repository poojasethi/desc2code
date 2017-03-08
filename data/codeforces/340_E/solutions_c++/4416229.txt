#include <iostream>
#include <vector>
using namespace std;

const long long M = 1e9 + 7;
int n, m;
long long o, p = 1;
int a[2001];
bool s[2001];
long long b[2001];

int main() {
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cin >> a[i];
    if (a[i] != -1)
      s[a[i]] = true;
  }
  for (int i = 1; i <= n; ++i)
    if (!s[i])
      if (a[i] == -1)
        ++m;
      else
        p = p * ++o % M;
  b[0] = p;
  b[1] = o * p % M;
  for (int i = 2; i <= m; ++i)
    b[i] = ((i - 1) * (b[i - 1] + b[i - 2]) + o * b[i - 1]) % M;
  cout << b[m] << endl;
}