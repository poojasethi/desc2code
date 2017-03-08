#include <cstdio>

int main() {
	int min, max, x;
	int n, m;

	scanf("%d %d", &n, &m);

	max = -1;

	for (int i = 0; i < n; i++) {
		min = 1000000005;

		for (int j = 0; j < m; j++) {
			scanf("%d", &x);

			if (x < min) min = x;
		}

		if (min > max) max = min;
	}

	printf("%d\n", max);

	return 0;
}
