#include <cstdio>
char b[2010][2010];
int t[2010][2010];
int to[2010][2010];
int y1, x1, y2, x2;
int dfs(int y, int x) {
	if (b[y][x] == '#') return t[y][x];
	if (t[y][x]) return t[y][x];
	t[y][x] = -1;
	int ny = y, nx = x, k;
	if (b[y][x] == '<') nx--;
	if (b[y][x] == '>') nx++;
	if (b[y][x] == '^') ny--;
	if (b[y][x] == 'v') ny++;
	k = dfs(ny, nx);
	if (k == -1) return -1;
	to[y][x] = b[ny][nx] == '#' ? to[y][x] : to[ny][nx];
	return t[y][x] = ++k;
}
int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s", b[i]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			to[i][j] = i * 3000 + j;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (b[i][j] != '#' && !t[i][j]) {
				dfs(i, j);
				if (t[i][j] == -1) {
					printf("-1\n");
					return 0;
				}
			}
		}
	}
	int mx = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (t[i][j] > t[y1][x1]) {
				y1 = i, x1 = j;
				mx = t[i][j];
			}
		}
	}
	if (mx == 0) {
		printf("0\n");
		return 0;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (t[i][j] == mx && to[i][j] != to[y1][x1]) {
				printf("%d\n", mx + mx);
				return 0;
			}
		}
	}
	printf("%d\n", mx + mx - 1);
	return 0;
}