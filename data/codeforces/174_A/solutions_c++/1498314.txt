#include <stdio.h>

int main() {
	int n, b; scanf("%d%d", &n, &b);

	int a[100], s = b;
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		s += a[i];
	}

	for (int i = 0; i < n; i++)
		if (s < a[i]*n) {
			puts("-1");
			return 0;
		}

	for (int i = 0; i < n; i++)
		printf("%.8lf\n", 1.*s/n - a[i]);

	return 0;
}
