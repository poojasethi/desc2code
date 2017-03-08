#include <stdio.h>
#include <string.h>

const int N = 1e3+10;
const int M = 4;
const char sign[M][M] = { "00", "01", "10", "11"};

int n, m, c[M], g[N][N];

void init() {
	char str[M];
	memset(g, 0, sizeof(g));
	memset(c, 0, sizeof(c));

	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%s", str);
			if (str[0] == '1' && str[1] == '1') c[2]++;
			else if (str[0] == '0' && str[1] == '0') c[0]++;
			else c[1]++;
		}
	}
}

void set() {
	for (int i = 0; i < n; i++) {
		if (i&1) {
			for (int j = m-1; j >= 0; j--) {
				if (c[2]) {
					g[i][j] = 3;
					c[2]--;
				} else if (c[1]) {
					g[i][j] = 1;
					c[1]--;
				}
				if (c[1] == 0 && c[2] == 0) return;
			}
		} else {
			for (int j = 0; j < m; j++) {
				if (c[2]) {
					g[i][j] = 3;
					c[2]--;
				} else if (c[1]) {
					g[i][j] = 2;
					c[1]--;
				}
				if (c[1] == 0 && c[2] == 0) return ;
			}
		}
	}
}

void solve() {
	set();
	for (int i = 0; i < n; i++) {
		printf("%s", sign[g[i][0]]);
		for (int j = 1; j < m; j++) printf(" %s", sign[g[i][j]]);
		printf("\n");
	}
}

int main () {
	init();
	solve();
	return 0;
}
