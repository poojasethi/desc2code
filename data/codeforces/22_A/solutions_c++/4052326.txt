#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  scanf("%d", &n);

  set<int> s;
  for (int i = 0, x; i < n; i++) {
    scanf("%d", &x);
    s.insert(x);
  }
  s.erase(s.begin());

  if (s.empty()) puts("NO");
  else printf("%d\n", *s.begin());

  return 0;
}
