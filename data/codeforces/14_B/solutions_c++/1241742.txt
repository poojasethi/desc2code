#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, x0; scanf("%d%d", &n, &x0);

	int r = 10000, l = -100;
	for (int i = 0; i < n; i++) {
		int a, b; scanf("%d%d", &a, &b);
		if (a > b) {
			int t = a; a = b; b = t;
		}
		if (b < r)
			r = b;
		if (a > l)
			l = a;
	}

	if (l > r) {
		puts("-1");
		return 0;
	}

	int m = 1000000;
	for (int i = l; i <= r; i++)
		if (abs(i - x0) < m)
			m = abs(i - x0);

	printf("%d\n", m);

	return 0;
}
