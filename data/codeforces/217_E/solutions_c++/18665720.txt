#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <climits>
#include <numeric>
#include <vector>
#include <ext/rope>
using namespace std;
using namespace __gnu_cxx;
crope s;
int n, k;
const int MAX_N = 5000 + 10;
int l[MAX_N], r[MAX_N];

crope build(int d, int L) {
	if (d < 0) {
		return s.substr(0, L);
	}
	int C = r[d] - l[d] + 1;
	//[l[d]+C,r[d]+C]
	int x = min(r[d] + C, L - 1) - (l[d] + C) + 1;
	if (x <= 0)
		return build(d - 1, L);
	crope t = build(d - 1, L - x);
	//[l[d],r[d]]
	char*buf = new char[x + 1];
	buf[x] = 0;
	for (int i = 0; i < x; ++i) {
		if (i * 2 + 1 < C)
			buf[i] = t[l[d] + i * 2 + 1];
		else
			buf[i] = t[l[d] + (i - C / 2) * 2];
	}
	t.insert(r[d] + 1, buf);
	return t;
}

char buf[int(3e6) + 10];

int main() {
	scanf("%s", buf);
	s = buf;
	cin >> k >> n;
	for (int i = 0; i < n; ++i) {
		cin >> l[i] >> r[i];
		--l[i], --r[i];
	}
	puts(build(n - 1, k).c_str());
	return 0;
}