#include <cstdio>
typedef long long ll;
int n, m, k, par[100010], sz[100010];
bool vis[100010];
int find(int x) {
	return par[x] == x ? x : par[x] = find(par[x]);
}
void merge(int x, int y) {
	int p = find(x), q = find(y);
	if ( p != q ) {
		par[p] = q;
		sz[q] += sz[p];
	}
}
int main() {
//	freopen("t.in", "r", stdin);
	scanf("%d%d%d", &n, &m, &k);
	for ( int i = 1; i <= n; i ++ ) {
		par[i] = i;
		sz[i] = 1;
	}
	for ( int i = 0; i < m; i ++ ) {
		int u, v;
		scanf("%d%d", &u, &v);
		if ( find(u) != find(v) )
			merge(u, v);
	}
	ll mul = 1, base = 0;
	int s = 0;
	for ( int i = 1; i <= n; i ++ )
		if ( !vis[find(i)] ) {
			vis[find(i)] = true;
			mul = mul * sz[find(i)] % k;
			base += sz[find(i)];
			s ++;
		}
	ll res = 1;
	for ( int i = 0; i < s - 2; i ++ )
		res = res * base % k;
	res = res * mul % k;
	if ( s > 1 )
		printf("%d\n", res);
	else
		printf("%d\n", 1 % k);
}
