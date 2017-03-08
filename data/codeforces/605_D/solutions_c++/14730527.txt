#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <numeric>
#include <cassert>
using namespace std;

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define forit(it,S) for(__typeof(S.begin()) it = S.begin(); it != S.end(); ++it)
#ifdef WIN32
#define I64d "%I64d"
#else
#define I64d "%lld"
#endif

typedef pair <int, int> pi;
typedef vector <int> vi;
typedef long long ll;

int a[111111], b[111111], c[111111], d[111111];
int from[111111];
int e[444444], en, n;
vector<pi> f[444444];
queue<int> q;

int Find(int x) {
  return lower_bound(e, e + en, x) - e;
}

void add(int x, pi pa) {
  while (x < en) {
    f[x].pb(pa);
    x = (x | (x + 1));
  }
}

int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d%d%d%d", &a[i], &b[i], &c[i], &d[i]);
    e[en++] = a[i];
    e[en++] = c[i];
  }
  e[en++] = 0;
  sort(e, e + en);
  en = unique(e, e + en) - e;

  for (int i = 0; i < n; i++) {
    int p = Find(a[i]);
    add(p, mp(b[i], i));
  }
  for (int i = 0; i < en; i++) {
    sort(f[i].begin(), f[i].end(), greater<pi>());
  }

  memset(from, -1, sizeof(from));
  q.push(n);
  while (!q.empty()) {
    int u = q.front();
    q.pop();

    int x = Find(c[u]);
    while (x >= 0) {
      while (!f[x].empty() && f[x].back().f <= d[u]) {
        int v = f[x].back().s;
        if (from[v] == -1) {
          from[v] = u;
          q.push(v);
        }
        f[x].pop_back();
      }
      x = (x & (x + 1)) - 1;
    }
  }

  if (from[n - 1] == -1) {
    puts("-1");
    return 0;
  }
  vi res;
  int u = n - 1;
  while (u != n) {
    res.pb(u);
    u = from[u];
  }
  reverse(res.begin(), res.end());
  printf("%d\n", int(res.size()));
  for (int i = 0; i < res.size(); i++) {
    if (i > 0) putchar(' ');
    printf("%d", res[i] + 1);
  }
  puts("");
  return 0;
}
