#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

double prob[101][4951], sum[101][4952], sum2[101][4952];

int main() {
  prob[0][0] = 1;

  for (int i = 1; i <= 100; ++i) {
    for (int j = (i - 1) * (i - 2) / 2; j >= 0; --j)
      for (int k = 0; k < i; ++k) prob[i][j + k] += prob[i - 1][j] / i;
  }

  for (int i = 1; i <= 100; ++i) {
    sum[i][0] = sum2[i][0] = 0;

    for (int j = 0; j <= i * (i - 1) / 2; ++j) {
      sum[i][j + 1] = sum[i][j] + prob[i][j];
      sum2[i][j + 1] = sum2[i][j] + prob[i][j] * j;
    }
  }

  int T, n, a[100];
  long long k;
  double dp[10000];

  scanf("%d", &T);

  while (T--) {
    scanf("%d %lld", &n, &k);

    for (int i = 0; i < n; ++i) scanf("%d", &a[i]);

    int inv = 0;

    for (int i = 0; i < n; ++i)
      for (int j = i + 1; j < n; ++j)
        if (a[i] > a[j]) ++inv;

    if (k >= inv)
      printf("0\n");
    else if (k == 0)
      printf("%d\n", inv);
    else {
      int m = n * (n - 1) / 2;

      dp[0] = m / 2.0;

      for (int i = 1; i < k; ++i) {
        dp[i] = 0;

        int r = (int)(i + floor(dp[i - 1]));

        if (r >= i + 1)
          dp[i] += sum2[n][r + 1] - sum2[n][i + 1] -
                   i * (sum[n][r + 1] - sum[n][i + 1]);

        if (r + 1 <= m) dp[i] += dp[i - 1] * (sum[n][m + 1] - sum[n][r + 1]);
      }

      printf("%.7f\n", min(dp[k - 1], (double)inv - k));
    }
  }

  return 0;
}