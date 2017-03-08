#include <fstream>
#include <iostream>
using namespace std;
#define ll long long

const int max_n = 1005;

ll aib[4][max_n][max_n];
int n, m;

void update (int x, int y, ll val) {
	int w = ((x & 1) * 2 + (y & 1));
	int cy = y;
	while (x <= n + 1) {
		y = cy;
		while (y <= n + 1) {
			aib[w][x][y] ^= val;
			y += y & (-y);
		}
		x += x & (-x);
	}
}
ll query (int x, int y) {
	if (x == 0 || y == 0)
		return 0;
	int w = ((x & 1) * 2 + (y & 1));
	int cy = y;
	ll rez = 0;
	while (x) {
		y = cy;
		while (y) {
			rez ^= aib[w][x][y];
			y -= y & (-y);
		}
		x -= x & (-x);
	}
    return rez;
}

int main() {
	cin >> n >> m;
	while (m--) {
		int t, x0, x1, y0, y1;
		ll val;
		cin >> t;
		cin >> x0 >> y0 >> x1 >> y1;
		if (t == 1) {
			ll rez = 0;
			rez ^= query(x0 - 1, y0 - 1);
			rez ^= query(x0 - 1, y1);
			rez ^= query(x1, y0 - 1);
			rez ^= query(x1, y1);
			cout << rez << '\n';
		} else {
			cin >> val;
 			update (x0, y0, val);
			update (x0, y1 + 1, val);
			update (x1 + 1, y0, val);
			update (x1 + 1, y1 + 1, val);
		}

	}
 	return 0;
}
