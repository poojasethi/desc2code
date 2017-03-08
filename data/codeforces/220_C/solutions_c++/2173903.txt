#include <iostream>
#include <set>
#include <algorithm>
#include <cstdio>

using namespace std;

const int N = 100010;
int b[N], p[N], n;

multiset < int > S;
int main () {
	int i, j, k;
	scanf ("%d", &n);
	for (i = 1; i <= n; i++) {
		scanf ("%d", &k);
		p[k] = i;
	}
	S.insert (- 100010); S.insert (100010);
	for (i = 1; i <= n; ++i) {
		scanf ("%d", &b[i]);
		S.insert (i - p[b[i]]);
	}
	for (i = 0; i < n; ++i) {
		multiset <int>::iterator it = S.lower_bound (i);
		int ans = 100010;
		ans = min (ans, *it - i); ans = min (ans, i - (* (-- it)));
		printf ("%d\n", ans);
		S.erase (S.find (i + 1 - p[b[i+1]] ));
		S.insert (n - p[b[i+1]] + i + 1);
	}
	return 0;
}

