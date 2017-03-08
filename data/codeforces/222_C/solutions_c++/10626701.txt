#include <bits/stdc++.h>

using namespace std;

int n, m;
int p[10000005];
int a[100005], b[100005];
int pa[10000005], pb[10000005];

void init(int *x, int *y, int len) {
	for (int i = 0; i < len; i++)
		for (int j = x[i]; j > 1; j /= p[j])
			y[p[j]]++;
}

void print(int *x, int *y, int len) {
	for (int i = 0; i < len; i++) {
		int cnt = 1;
		for (int j = x[i]; j > 1; j /= p[j])
			if (y[p[j]]) y[p[j]]--;
			else cnt *= p[j];
		cout << cnt << " \n"[i == len - 1];
	}
}

int main() {
	// freopen("c.in", "r", stdin);
	cin >> n >> m;
	cout << n << ' ' << m << endl;
	for (int i = 2; i <= 10000000; i++) {
		if (!p[i]) {
			p[i] = i;
			for (int j = i + i; j <= 10000000; j += i)
				p[j] = i;
		}
	}
	for (int i = 0; i < n; i++) cin >> a[i];
	for (int i = 0; i < m; i++) cin >> b[i];
	init(a, pa, n);
	init(b, pb, m);
	print(a, pb, n);
	print(b, pa, m);

	return 0;
}
