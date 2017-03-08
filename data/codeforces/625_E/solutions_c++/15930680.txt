#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <queue>
#define Rep(i, x, y) for (int i = x; i <= y; i ++)
#define make make_pair<int, int>
using namespace std;
typedef long long LL;
typedef double DB;
const int N = 120000;
struct arr { int p, z, n; } a[N];
int n, m, pl[N], nex[N], ans[N], az, pre[N], w[N]; bool c[N], vis[N];
LL add[N];
priority_queue< pair<int, int> > q;
bool cmp(arr x, arr y) { return x.p < y.p; }
int Find(int x, int k) {
	if (x == k) return 0;
	LL l = a[k].p - a[x].p; if (l <= 0) l = m + l;
	l += add[k] - add[x];
	int t = 0;
	if (a[x].n < a[k].n) l -= a[x].z, t = 1;
	if (l <= 0 && !add[x] && !add[k]) return 1;
	else if (a[k].z < a[x].z) return (l - 1) / (a[x].z - a[k].z) + t + 1;
	return 0;
}
int main()
{
	scanf ("%d%d", &n, &m);
	Rep(i, 1, n) {
		scanf ("%d%d", &a[i].p, &a[i].z);
		a[i].n = i, c[i] = 1;
	}
	sort(a + 1, a + n + 1, cmp);
	Rep(i, 1, n) pl[ a[i].n ] = i;
	Rep(j, 1, n) {
		int i = pl[j], k = i % n + 1, z;
		z = Find(i, k); nex[i] = k, pre[k] = i;
		if (z) q.push( make(-z, -j) ), w[i] = z;
	}
	while (!q.empty()) {
		int x = pl[ -(q.top()).second ], z = -(q.top()).first, num = 1; q.pop();
		if (!c[x] || w[x] != z) continue ;
		c[ nex[x] ] = 0, nex[x] = nex[ nex[x] ];
		for (; Find(x, nex[x]) == z; ) c[ nex[x] ] = 0, nex[x] = nex[ nex[x] ], num ++;
		a[x].z = max(a[x].z - num, 0), pre[ nex[x] ] = x;
		add[x] += (LL)num * z;
		z = Find(x, nex[x]);
		if (z) q.push( make(-z, -a[x].n) ), w[x] = z; else w[x] = 0;
		z = Find(pre[x], x);
		if (z) q.push( make(-z, -a[ pre[x] ].n) ), w[ pre[x] ] = z;
	}
	Rep(i, 1, n) if (c[i]) ans[++ az] = a[i].n;
	printf("%d\n", az);
	Rep(i, 1, az) printf("%d ", ans[i]);
	puts("");

	return 0;
}