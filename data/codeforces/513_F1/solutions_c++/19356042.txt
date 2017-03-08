#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#define mset(x, a) memset(x, a, sizeof(x))
using namespace std;
typedef long long ll;
inline int read() {
	char ch = getchar(); int x = 0;
	while(ch < '0' || ch > '9') ch = getchar();
	while(ch >= '0' && ch <= '9') x = x*10+ch-'0', ch = getchar();
	return x;
}

const int maxn = 2005, inf = 1e9;
const int fx[4] = { 0, 0, -1, 1 };
const int fy[4] = { -1, 1, 0, 0 };
int N, M, S, T, C1, C2, sum, level[maxn], iter[maxn];
ll dis[maxn][maxn];
struct Point {
	int x, y, t;
	void init() { x = read(), y = read(), t = read(); }
} d1[maxn], d2[maxn], O;
char s[maxn][maxn];
bool check[maxn];
struct Edge { int to, cap, rev; };
vector <Edge> G[maxn];

inline int P(int x, int y, int z) { return C1+C2+z*N*M + (x-1)*M+y; }
void fail() { printf("-1\n"); exit(0); }
void add(int x, int y, int c) {
	G[x].push_back((Edge){ y, c, G[y].size() });
	G[y].push_back((Edge){ x, 0, G[x].size()-1});
}

void Input() {
	N = read(), M = read(), C1 = read(), C2 = read();
	if((C1+C2)%2 == 0) fail();
	for(int i = 1; i <= N; ++i) {
		scanf("%s", s[i]+1);
		for(int j = 1; j <= M; ++j) sum += (s[i][j] == '.');
	}
	
	O.init();
	for(int i = 1; i <= C1; ++i) d1[i].init();
	for(int i = 1; i <= C2; ++i) d2[i].init();
	if(C1 > C2) {
		for(int i = 1; i <= C1; ++i) swap(d1[i], d2[i]);
		swap(C1, C2);
	}
	if(C1+1 != C2 || sum < C2) fail();
	d1[++C1] = O;
	
	S = 0, T = C1+C2+2*N*M+1;
}

void Bfs(int x, int y) {
	int now = P(x, y, 0);
	mset(check, 0);
	queue <Point> q;
	dis[now][now] = 0;
	q.push((Point){ x, y });
	check[now] = true;
	
	while(!q.empty()) {
		Point v = q.front(); q.pop();
		int num = P(v.x, v.y, 0);
		for(int d = 0; d < 4; ++d) {
			int nx = v.x+fx[d], ny = v.y+fy[d], nnum = P(nx, ny, 0);
			if(!nx || !ny || nx > N || ny > M || check[nnum] || s[nx][ny] == '#') 
				continue;
			dis[now][nnum] = dis[now][num]+1;
			check[nnum] = true;
			q.push((Point){ nx, ny });
		}
	}
}

void Getdis() {
	mset(dis, 63);
	for(int i = 1; i <= N; ++i)
	for(int j = 1; j <= M; ++j)
		if(s[i][j] == '.') Bfs(i, j);
}

bool bfs() {
	mset(level, -1), mset(iter, 0);
	queue <int> q;
	level[S] = 0; q.push(S);
	while(!q.empty()) {
		int v = q.front(); q.pop();
		for(int i = 0; i < G[v].size(); ++i) {
			Edge &e = G[v][i];
			if(e.cap && level[e.to] < 0)
				level[e.to] = level[v]+1, q.push(e.to);
		}
	}
	return level[T] > 0;
}

int dfs(int v, int f) {
	if(v == T || !f) return f;
	for(int &i = iter[v]; i < G[v].size(); ++i) {
		Edge &e = G[v][i];
		if(e.cap && level[e.to] > level[v]) {
			int d = dfs(e.to, min(f, e.cap));
			if(d) { e.cap -= d, G[e.to][e.rev].cap += d; return d; }
		}
	}
	return 0;
}

int MaxFlow() {
	int flow = 0;
	while(bfs()) 
		for(int f; (f = dfs(S, inf)) > 0; ) flow += f;
	return flow;
}

bool Judge(ll x) {
	for(int i = S; i <= T; ++i) G[i].clear();
	for(int i = 1; i <= N; ++i)
	for(int j = 1; j <= M; ++j)
		add(P(i, j, 0), P(i, j, 1), 1);
	
	for(int k = 1; k <= C1; ++k) {
		add(S, k, 1);
		ll d = x/d1[k].t;
		for(int i = 1; i <= N; ++i)
		for(int j = 1; j <= M; ++j)
			if(dis[P(d1[k].x, d1[k].y, 0)][P(i, j, 0)] <= d)
				add(k, P(i, j, 0), 1);			
	}
	
	for(int k = 1; k <= C2; ++k) {
		add(C1+k, T, 1);
		ll d = x/d2[k].t;
		for(int i = 1; i <= N; ++i)
		for(int j = 1; j <= M; ++j)
			if(dis[P(d2[k].x, d2[k].y, 0)][P(i, j, 0)] <= d)
				add(P(i, j, 1), C1+k, 1);
	}
	return MaxFlow() == C1;
}

ll Solve() {
	ll l = 0, r = 1e13, ans = -1;
	while(l <= r) {
		ll mid = (l+r)>>1;
		if(Judge(mid)) ans = mid, r = mid-1;
		else l = mid+1;
	}
	return ans;
}

int main() {
	Input();
	Getdis();
	printf("%I64d\n", Solve());
	return 0;
}
