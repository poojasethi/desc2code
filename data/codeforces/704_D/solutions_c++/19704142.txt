#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define rep(i,a,b) for(int i = (a); i <= (b); i++)//(a)!
#define dep(i,a,b) for(int i = (a); i >= (b); i--)
#define ab(a) ((a) > 0 ? (a) : -(a))
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back(a)
using namespace std;
typedef long long LL;
typedef unsigned long long uLL;

const int N = 400010, inf = 1000000000;
int r, b, eid[N]; 
int n, m; 	
bool fl = false;
namespace flow{
	int S, T, SS, TT;
	struct edge{ int to, pre, w; } e[N * 7]; int u[N], l = 1;
	void ins(int a, int b, int w) { e[++l] = (edge){b, u[a], w}, u[a] = l; }
	void insert(int a, int b, int w) { ins(a, b, w), ins(b, a, 0); }
	int Sx[N], xT[N];
	void insert(int a, int b, int l, int r) { Sx[b] += l, xT[a] += l, insert(a, b, r - l); }
	void build() {
		SS = 1, TT = T + 1;
		rep(i,S,T) { if (Sx[i]) insert(SS, i, Sx[i]); if (xT[i]) insert(i, TT, xT[i]); }
	}
	#define v e[i].to
	#define ew e[i].w
	#define reg(i,a) for(int i = u[a]; i; i = e[i].pre)
	
	int h[N], q[N], cur[N];
	bool bfs() {
		int l = 0, r = 1;
		rep(i,SS,TT) h[i] = -1; q[ h[SS] = 0 ] = SS;
		while (l < r) {
			int x = q[l++];
			reg(i,x) if (ew && h[v] == -1) h[v] = h[x] + 1, q[r++] = v;
		}
		return h[TT] != -1;
	}
	
	int dfs(int x, int f) {
		if (!f || x == TT) return f;
		int used = 0, w;
		for(int i = cur[x]; i; i = e[i].pre) if (h[v] == h[x] + 1 && ew) {
			w = min(ew, f - used), w = dfs(v, w);
			ew -= w; if (ew) cur[x] = i;
			e[i^1].w += w;
			used += w; if (used == f) break;
		} 
		if (!used) h[x] = -1;
		return used;
	}
	
	void dinic() {
		while (bfs()) {
			rep(i,SS,TT) cur[i] = u[i];
			dfs(SS, inf);
		}
	}
	
	
	void work() {
		dinic();
		insert(T, S, inf);
		dinic();
		reg(i,SS) if (ew) { printf("-1\n"); return; }
		int t = e[l].w;
		cout << 1LL * r * t + 1LL * b * (n - t) <<endl;
		rep(j,1,n) {
			int i = eid[j]; bool tmp = ew;
			if (tmp ^ fl) printf("r"); else printf("b");
		}
		printf("\n");
	}
}

int find(int *a, int x) {
	int l = 1, r = n + 1;
	while (l + 1 < r) {
		int mid = (l + r) >> 1;
		if (a[mid] <= x) l = mid; else r = mid;
	}
	return l;
}

int x[N], y[N];
int dx[N], dy[N], cx[N], cy[N], b1[N], c1[N];

int main() {
	scanf("%d%d",&n,&m);
	scanf("%d%d",&r,&b); if (r < b) swap(r, b), fl = true;
	rep(i,1,n) scanf("%d%d",&x[i],&y[i]), b1[i] = x[i], c1[i] = y[i];
	sort(b1 + 1, b1 + n + 1); sort(c1 + 1, c1 + n + 1);
	rep(i,1,n) x[i] = find(b1, x[i]), y[i] = find(c1, y[i]), cx[x[i]]++, cy[y[i]]++;
	rep(i,1,n) dx[i] = cx[i], dy[i] = cy[i];
	rep(i,1,m) {
		int t, l, d; scanf("%d%d%d",&t,&l,&d); int tmp = l;
		if (t == 1) {
			l = find(b1, l);
			if (b1[l] == tmp) dx[l] = min(dx[l], d); 
		} else {
			l = find(c1, l);
			if (c1[l] == tmp) dy[l] = min(dy[l], d);
		}
	}
	int &S = flow::S, &T = flow::T;
	S = 2, T = n * 2 + 3;
	rep(i,1,n) {
		flow::insert(x[i] + 2, y[i] + n + 2, 0, 1);
		eid[i] = flow::l;
	}
	rep(i,1,n) {
		int d = dx[i], c = cx[i]; 
		int l = (c - d) / 2 + (c - d) % 2, r = (c + d) / 2;// cout <<c<<' '<<d<<' '<<l<<' '<<r<<endl;
		if (l > r) { printf("-1\n"); return 0; }
		flow::insert(S, i + 2, l, r);
	}
	rep(i,1,n) {
		int d = dy[i], c = cy[i];
		int l = (c - d) / 2 + (c - d) % 2, r = (c + d) / 2;// cout <<c<<' '<<d<<' '<<l<<' '<<r<<endl;
		if (l > r) { printf("-1\n"); return 0; }
		flow::insert(i + n + 2, T, l, r);
	}
	flow::build();
	flow::work();
	return 0;
}