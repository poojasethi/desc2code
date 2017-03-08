#include <stdio.h>
#include <string.h>

typedef long long ll;

const ll mod = 1e9 + 7;
int n, b, k, x, O[10];
ll A[110][110];

void arrMul(ll a[110][110], ll b[110][110]) {
  ll c[110][110];
  memset(c, 0, sizeof(c));
  for (int i = 0 ; i < x ; ++i) {
    for (int j = 0 ; j < x ; ++j) {
      for (int k = 0 ; k < x ; ++k) {
        c[i][j] += a[i][k] * b[k][j];
        c[i][j] %= mod;
      }
    }
  }
  for (int i = 0 ; i < x ; ++i) {
    for (int j = 0 ; j < x ; ++j) {
      a[i][j] = c[i][j];
    }
  }
}

int main() {
  scanf("%d%d%d%d", &n, &b, &k, &x);
  for (int i = 0 ; i < n ; ++i) {
    int num;
    scanf("%d", &num);
    ++O[num];
  }
  for (int i = 0 ; i < x ; ++i) {
    for (int j = 0 ; j < 10 ; ++j) {
      A[i][(i * 10 + j) % x] += O[j];
    }
  }
  ll S[110][110];
  memset(S, 0, sizeof(S));
  for (int i = 0 ; i < x ; ++i) {
    S[i][i] = 1;
  }
  while (b) {
    if (b & 1) {
      arrMul(S, A);
    }
    arrMul(A, A);
    b >>= 1;
  }
  printf("%lld\n", S[0][k]);
}