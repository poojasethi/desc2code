#include <iostream>
#include <utility>
#include <cmath>
#include <algorithm>
#include <limits>
using namespace std;

const int MaxN = 1e5;
int N;
pair<long double, int> list[MaxN];

int main() {
	ios::sync_with_stdio(0);

	cin >> N;
	for (int i = 0; i < N; i ++) {
		int x, y;
		cin >> x >> y;
		list[i].first = atan2((long double)y, x);
		list[i].second = i + 1;
	}

	sort(list, list + N);

	long double ans = 2*M_PI;
	int index = 1;
	for (int i = 0; i < N; i ++) {
		long double d = abs(list[i].first - list[(i + 1) % N].first);
		if (min(d, 2*M_PI - d) < ans) {
			ans = min(d, 2*M_PI - d);
			index = i;
		}
	}

	cout << list[index].second << " " << list[(index + 1) % N].second << endl;

	return 0;
}

