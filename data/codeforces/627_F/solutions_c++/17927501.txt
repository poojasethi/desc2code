#include <bits/stdc++.h>
#define ll long long
#define clr(a) memset(a, 0, sizeof(a));
using namespace std;

const int MaxN = 200010, MaxM = 400010;
const ll inf = 1ll << 60;

class Graph {
public:
	int en[MaxN], next[MaxM], to[MaxM], tot;
	void add_edge(int x, int y) {
		next[++tot] = en[x];
		en[x] = tot;
		to[tot] = y;
	}
}	G;
int n, a[MaxN], b[MaxN];
int edge_u, edge_v;
bool diff[MaxN];
ll step;

inline bool check() {
	for (int i = 1; i <= n; ++i)
		if (a[i] != b[i]) return 0;
	return 1;
}

int cycle[MaxN], ctot;

bool vis[MaxN], flag;
int father[MaxN], depth[MaxN];
void dfs_init(int now) {
	vis[now] = 1;
	for (int i = G.en[now]; i; i = G.next[i])
		if (!vis[G.to[i]]) {
			father[G.to[i]] = now;
			depth[G.to[i]] = depth[now] + 1;
			dfs_init(G.to[i]);
		}
}
int get_lca(int u, int v) {
	while (u != v) {
		if (depth[u] > depth[v]) u = father[u];
		else v = father[v];
	}
	return u;
}
int get_dist(int l, int u) {
	return depth[u] - depth[l];
}

void dfs_edge(int now) {
	vis[now] = 1;
	int deg = 0;
	for (int i = G.en[now]; i; i = G.next[i])
		if (diff[G.to[i]]) {
			++deg;
			if (!vis[G.to[i]]) dfs_edge(G.to[i]);
		}
	if (deg == 1) {
		if (edge_u) edge_v = now;
		else edge_u = now;
	}
	if (deg > 2) flag = 1;
}

void dfs_cycle(int now) {
	cycle[++ctot] = now;
	vis[now] = 1;
	for (int i = G.en[now]; i; i = G.next[i])
		if (!vis[G.to[i]] && diff[G.to[i]]) dfs_cycle(G.to[i]);
}

int get_deg(int u) {
	int deg = 0;
	for (int i = G.en[u]; i; i = G.next[i])
		deg += diff[G.to[i]];
	return deg;
}

int pos[MaxN];
void solve_cycle(int in, int out) {
	for (int u = 1; u <= n; ++u) 
		if (get_deg(u) == 2) diff[u] = 1;
	clr(vis);
	dfs_edge(in);
	if (flag) return;
	if (edge_u > edge_v) swap(edge_u, edge_v);
	G.add_edge(edge_u, edge_v);
	G.add_edge(edge_v, edge_u);
	clr(vis);
	dfs_cycle(in);

	if (!vis[out]) return;
	int node = 0;
	for (int i = 1; i <= ctot; ++i)
		if (cycle[i] != out) {
			pos[b[cycle[i]]] = ++node;
		}
	int delta = pos[a[cycle[2]]] - 1;
	for (int i = 2; i <= ctot; ++i) {
		int tmp = pos[a[cycle[i]]] - i + 1;
		if (tmp < 0) tmp += ctot - 1;
		if (tmp != delta) return;
	}
	
	int post = 0;	
	for (int i = 1; i <= ctot; ++i)
		if (cycle[i] == out) post = i;
	ll now = inf, st;
	st = 1ll * delta * ctot - (post - 1);
	if (st < 0) st = -st;
	now = min(now, st);
	st = 1ll * (ctot - delta - 1) * ctot + (post - 1);
	if (st < 0) st = -st;
	now = min(now, st);
	step += now;
	for (int i = 1; i <= ctot; ++i) a[cycle[i]] = b[cycle[i]];
}

void go(int& s, int *a, int *b) {
	while (true) {
		int pos = 0, deg = 0;
		for (int i = G.en[s]; i; i = G.next[i])
			if (a[G.to[i]] != b[G.to[i]]) {
				++deg;
				if (a[G.to[i]] == b[s]) pos = G.to[i];
			}
		if (!pos || (deg != 1)) return;
		swap(a[s], a[pos]);
		s = pos;
		++step;
	}
}

int bfs(int& s) {
	static int q[MaxN], dist[MaxN];
	int l = 0, r = 0;
	memset(dist, 63, sizeof(dist));
	q[++r] = s;
	dist[s] = 0;
	while (l != r) {
		int u = q[++l];
		for (int i = G.en[u]; i; i = G.next[i])
			if (dist[G.to[i]] > dist[u] + 1) {
				dist[G.to[i]] = dist[u] + 1;
				q[++r] = G.to[i];
				if (diff[G.to[i]]) {
					s = u;
					return dist[u];
				}
			}
	}
	return -1;
}

int main() {
	int s, t;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		scanf("%d", a + i);
		if (a[i] == 0) s = i;
	}
	for (int i = 1; i <= n; ++i) {
		scanf("%d", b + i);
		if (b[i] == 0) t = i;
	}
	for (int i = 1; i < n; ++i) {
		int u, v;
		scanf("%d%d", &u, &v);
		G.add_edge(u, v);
		G.add_edge(v, u);
	}
	int ss = s, tt = t;
	go(s, a, b);
	if (check()) {
		printf("0 %I64d\n", step);
		return 0;
	}
	go(t, b, a);
	if ((a[t] == b[s]) && (a[s] == b[t])) {
		swap(a[t], a[s]);
		if (check()) {
			printf("%d %d %I64d\n", min(s, t), max(s, t), step + 1);
			return 0;
		}
		swap(a[t], a[s]);
	}
	int root = 0;
	for (int i = 1; i <= n; ++i) {
		diff[i] = (a[i] != b[i]);
		if (diff[i]) root = i;
	}
	clr(vis);
	dfs_init(root);
	if (a[s] == b[s]) {
		int l = get_lca(ss, tt);
		step = get_dist(l, ss) + get_dist(l, tt);
		step += 2 * bfs(l);
		solve_cycle(l, l);
	} else solve_cycle(s, t);
	if (!check()) printf("-1\n");
	else printf("%d %d %I64d\n", edge_u, edge_v, step);
	return 0;
}