#include <stdio.h>
#include <string.h>

int max(int a, int b) { return a > b ? a : b; }

int main() {
	int n, h; scanf("%d%d", &n, &h);

	long long c[36][36];
	memset(c, 0, sizeof(c));
	c[0][0] = 1;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= h; j++) {
			c[i][j] = 0;
			for (int l = 0; l <= i-1; l++) {
				int jj = max(j-1, 0);
				c[i][j] += c[l][jj]*c[i-1-l][0] + c[l][0]*c[i-1-l][jj] - c[l][jj]*c[i-1-l][jj];
			}
		}
	}

	printf("%I64d\n", c[n][h]);

	return 0;
}
