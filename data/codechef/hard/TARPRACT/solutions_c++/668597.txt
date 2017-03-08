#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long double ld;

ld vet[3];
ld *prob = vet + 1;
ld memo[2 << 18]; // extra bit: mask size

#define INF 1e100

ld solve(int mask, int n) {
  // mask == 111...1, everyone is dead
  if (mask == (1 << n) - 1) {
    return 0;
  }
  // memoization
  ld& res = memo[mask | (1 << n)]; // extra bit: mask size
  if (res) {
    return res;
  }
  res = INF;
  // each shot
  for (int i = 0; i < n; i++) {
    ld num = 1, den = 1;
    bool good = false;
    for (int j = -1; j <= 1; j++) {  // left, straigth, right
      int index = i + j;
      int mask_index = 1 << index;
      if (index < 0 || index == n || (mask & mask_index)) {
        // nothing to kill
        den -= prob[j];
        continue;
      }
      good = true;  // at least one killed
      ld next;
      int right_is_dead = (mask << 1) & mask_index,
          left_is_dead = (mask >> 1) & mask_index,
          right_part = mask & (mask_index - 1),
          left_part = mask >> index,
          nright = index,
          nleft = n - index;
      if (right_is_dead) {
        if (left_is_dead) {
          next = solve(right_part, nright) +
                 solve(left_part >> 1, nleft - 1); // one bit less
        } else { // right is alive
          next = solve(right_part, nright) +
                 solve(left_part | 1, nleft);
        }
      } else if (left_is_dead) { // only right is alive
        next =
          solve(right_part | mask_index, nright + 1) +
          solve(left_part >> 1, nleft - 1);
      } else {
        next = solve(mask | mask_index, n);
      }
      num += prob[j] * next;
    }
    if (good) {
      res = min(res, num / den);
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  while (T--) {
    memset(memo, 0, sizeof(memo));
    int n;
    cin >> n >> vet[0] >> vet[1] >> vet[2];
    vet[0] /= 100;
    vet[1] /= 100;
    vet[2] /= 100;
    ld res = solve(0, n);
    printf("%.6Lf\n", res);
  }
}
