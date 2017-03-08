#include <stdio.h>

int main() {
  int n, a[65], length = 0;
  scanf("%d", &n);
  while (n) {
    int t = n, m = 0, p = 1;
    while (t) {
      if (t % 10) m += p;
      t /= 10;
      p *= 10;
    }
    a[length++] = m;
    n -= m;
  }
  printf("%d\n", length);
  for (int i = 0; i < length; i++) {
    printf("%d ", a[i]);
  }
  return 0;
}
