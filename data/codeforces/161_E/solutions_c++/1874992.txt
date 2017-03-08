#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

char s[32];
long long ret;
int t, n, p, m[10][10], prim[1000010];

void gao(int i, int j) {
	if (i == n - 1) {
		long long cnt = 1;
		for (int ii = 1; ii < n; ++ii) {
			int cc = 0;
			for (int d = 0; d <= 9; ++d) {
				int num = 0;
				m[ii][ii] = d;
				for (int jj = 0; jj < n; ++jj)
					num = num * 10 + m[ii][jj];
				cc += prim[num];
			}
			cnt *= cc;
		}
		ret += cnt;
	} else {
		for (int d = 0; d <= 9; ++d) {
			m[i][j] = m[j][i] = d;
			if (j < n - 1) {
				gao(i, j + 1);
			} else {
				bool can_prim = false;
				for (int dd = 0; dd <= 9; ++dd) {
					int num = 0;
					m[i][i] = dd;
					for (int jj = 0; jj < n; ++jj)
						num = num * 10 + m[i][jj];
					if (prim[num]) {
						can_prim = true;
						break;
					}
				}
				if (can_prim) {
					gao(i + 1, i + 1 + 1);
				}
			}
		}
	}
}

int main() {
	// Compute prims
	for (int i = 0; i <= 1000000; ++i)
		prim[i] = 1;
	prim[0] = prim[1] = 0;
	for (int i = 2; i <= 1000000; ++i) {
		if (prim[i]) {
			for (int j = i + i; j <= 1000000; j += i)
				prim[j] = 0;
		}
	}
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		scanf("%s", s);
		n = strlen(s);
		for (int i = 0; i < n; ++i)
			m[0][i] = m[i][0] = s[i] - '0';
		ret = 0;
		gao(1, 2);
		cout << ret << endl;
	}
	return 0;
}
