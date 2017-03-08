#include <stdio.h>
#include <string.h>

int min(int a, int b) {
	return a < b ? a : b;
}

typedef struct { int c, p, a, b; } result;
result r[1<<7][100][100];

char b[100][100];

void backtrace(int mask, int i, int j) {
	b[i][j] = 'X';
	result c = r[mask][i][j];
	if (c.p == 1) {
		backtrace(c.a, i, j);
		backtrace(c.b, i, j);
	} else if (c.p == 2)
		backtrace(mask, c.a, c.b);
}

int main() {
	int n, m, k; scanf("%d%d%d", &n, &m, &k);

	int a[n][m];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &a[i][j]);

	const int inf = 1000000000;
	for (int mask = 0; mask < 1<<k; mask++)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				r[mask][i][j].c = inf;
	
	for (int i = 0; i < k; i++) {
		int x, y; scanf("%d%d", &x, &y); x--; y--;
		r[1<<i][x][y] = (result){a[x][y], 0, 0, 0};
	}

	for (int mask = 0; mask < 1<<k; mask++) {
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				for (int submask = mask; submask > 0; submask = mask & (submask-1)) {
					int c = r[submask][i][j].c + r[mask ^ submask][i][j].c - a[i][j];
					if (c < r[mask][i][j].c)
						r[mask][i][j] = (result){c, 1, submask, mask ^ submask};
				}
			}

		for (int l = 0; l < n*m; l++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < m; j++) {
					for (int di = 0; di < 4; di++) {
						int ii = i + (const int[]){1, 0, -1, 0}[di],
						    jj = j + (const int[]){0, 1, 0, -1}[di];
						if (0 <= ii && ii < n && 0 <= jj && jj < m) {
							int c = r[mask][i][j].c + a[ii][jj];
							if (c < r[mask][ii][jj].c)
								r[mask][ii][jj] = (result){c, 2, i, j};
						}
					}
				}
	}

	int mc = inf, mi, mj;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			int c = r[(1<<k)-1][i][j].c;
			if (c < mc) {
				mc = c; mi = i; mj = j;
			}
		}

	memset(b, '.', sizeof(b));
	backtrace((1<<k)-1, mi, mj);

	printf("%d\n", mc);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			putchar(b[i][j]);
		putchar('\n');
	}

	return 0;
}
