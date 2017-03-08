#include <cstdio>
#include <algorithm>
using namespace std;

int n, m, d, h;
int ans = 0, _d, _h;

int main() {

	scanf("%d%d", &n, &m);
	scanf("%d%d", &_d, &_h);
	ans = _h + _d - 1;

	for (int i = 1; i < m; ++i) {
		scanf("%d%d", &d, &h);
		int dD = d - _d;
		int dH = h - _h;
		if (dD < abs(dH)) {
			puts("IMPOSSIBLE");
			return 0;
		}
		ans = max(ans, _h + (dD + dH) / 2),
			_d = d, _h = h;

	}
	printf("%d", max(ans, _h + n - _d));
	return 0;
}