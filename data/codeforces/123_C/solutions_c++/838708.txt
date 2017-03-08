#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

const int MAX_N = 110;
const int MAX_PRI = 1000000;
const long long INF = 1000000000000000001LL;

int n, m, len;
long long k;
int priority[2*MAX_N];
int index[2*MAX_N];
long long dp[2*MAX_N][2*MAX_N];
char sol[2*MAX_N];

int cmp(int i, int j) {
  return priority[i] < priority[j];
}

int main() {
#ifndef ONLINE_JUDGE
  ifstream cin("c.in");
#endif

  cin >> n >> m >> k;
  len = n+m-1;
  for (int i = 1; i <= len; ++i) {
    priority[i] = MAX_PRI;
    index[i] = i;
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      int x;
      cin >> x;
      priority[i+j-1] = min(priority[i+j-1], x);
    }
  }

  sort(index+1, index+len+1, cmp);

  for (int i = 1; i <= len; ++i) {
    sol[index[i]] = '(';
    dp[0][0] = 1;
    for (int x = 1; x <= len; ++x)
      for (int y = 0; y <= len; ++y) {
        dp[x][y] = 0;
        if (y > 0 && sol[x] != ')') {
          dp[x][y] += dp[x-1][y-1];
        }
        if (sol[x] != '(') {
          dp[x][y] += dp[x-1][y+1];
        }
        dp[x][y] = min(dp[x][y], INF);
      }

    if (k > dp[len][0]) {
      k -= dp[len][0];
      sol[index[i]] = ')';
    }
  }

  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      printf("%c", sol[i+j-1]);
    }
    printf("\n");
  }

  return 0;
}
