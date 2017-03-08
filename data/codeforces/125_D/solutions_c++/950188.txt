#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;

#define pb push_back

const int N = 30005;
const int INF = 0x3fffffff;

int A[N];

void print(vector<int> &x) {
	for (int i = 0; i < x.size(); i++) {
		printf("%d ", x[i]);
	}
	puts("");
}
void print(vector<int> &x, vector<int> &y) {
	if (y.empty()) {
		y.push_back(x.back());
		x.pop_back();
	}
	print(x);
	print(y);
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int n;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		scanf("%d", &A[i]);
	}

	int d = A[n - 1] - A[n - 2];
	int la = n - 2;
	while (la && A[la] - A[la - 1] == d) {
		la--;
	}

	for (int t = 0; t < 3; t++) {
		vector<int> x, y;
		if (!t) {
			x.pb(A[0]), x.pb(A[1]);
		} else if (t == 1) {
			x.pb(A[0]), x.pb(A[2]), y.pb(A[1]);
		} else {
			x.pb(A[1]), x.pb(A[2]), y.pb(A[0]);
		}

		int dy = INF;
		int dx = x[1] - x[0];
		for (int i = (t == 0) ? 2 : 3; i <= n; i++) {
			if (i == n) {
				print(x, y);
				return 0;
			}
			if (i >= la) {
				if (y.size() == 1 && A[i] - y.back() == d || dy == d && A[i] - y.back() == d && d == dy) {
					y.insert(y.end(), &A[i], A + n);
					print(x, y);
					return 0;
				} else if (x.back() + dx == A[i] && dx == d) {
					x.insert(x.end(), &A[i], A + n);
					print(x, y);
					return 0;
				}
			}
			if (x.back() + dx == A[i]) {
				x.push_back(A[i]);
			} else if (dy == INF || y.back() + dy == A[i]) {
				y.push_back(A[i]);
				if (y.size() == 2) {
					dy = y[1] - y[0];
				}
			} else {
				break;
			}
		}
	}

	cout << "No solution" << endl;
	return 0;
}