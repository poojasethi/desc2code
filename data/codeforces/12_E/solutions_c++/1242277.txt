#include <stdio.h>

int main() {
	int n; scanf("%d", &n);

	int a[n][n];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			a[i][j] = 1 + (i+j) % (n-1);

	for (int i = 0; i < n; i++) {
		a[n-1][i] = a[i][n-1] = a[i][i];
		a[i][i] = 0;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			printf("%d ", a[i][j]);
		putchar('\n');
	}

	return 0;
}
