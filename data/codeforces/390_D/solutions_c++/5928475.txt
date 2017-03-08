#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;
const int N = 10005;
struct state {
	int x, y;
}p[N];
int n, m, k, c;

bool cmp(const state& a, const state& b) {
	return a.x + a.y < b.x + b.y;
}

void init () {
	c = 0;
	scanf("%d%d%d", &n, &m, &k);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			p[c].x = i; p[c].y = j; c++;
		}
	}
	sort (p, p + c, cmp);
}

void handle(int x, int y) {
	for (int i = 1; i <= x; i++) printf("(%d,1) ", i);
	for (int i = 2; i <= y; i++) printf("(%d,%d) ", x, i);
	printf("\n");
}

void solve () {
	int ans = 0;
	for (int i = 0; i < k; i++) 
		ans += p[i].x + p[i].y - 1;
	printf("%d\n", ans);
	for (int i = k-1; i >= 0; i--) {
		handle(p[i].x, p[i].y);
	}
}

int main () {
	init();
	solve ();
	return 0;
}
