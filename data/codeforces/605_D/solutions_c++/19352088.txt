#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;
inline int read() {
	char ch = getchar(); int x = 0;
	while(ch < '0' || ch > '9') ch = getchar();
	while(ch >= '0' && ch <= '9') x = x*10+ch-'0', ch = getchar();
	return x;
}

const int maxn = 2e5+5;

int N, M, back, h[maxn], prev[maxn], dis[maxn], ans[maxn];
struct Paper {
	int a, b, c, d;
	void init() { a = read(), b = read(), c = read(), d = read(); }
	void update() { a = lower_bound(h+1, h+1+M, a)-h, c = lower_bound(h+1, h+1+M, c)-h; }
} p[maxn];

vector <int> t[maxn];
bool cmp(int x, int y) { return p[x].b > p[y].b; }

void insert(int x, int v) {
	while(x <= M) t[x].push_back(v), x += x&-x;
}

int main() {
	N = read();
	for(int i = 1; i <= N; ++i) p[i].init();
	for(int i = 0; i <= N; ++i) h[++M] = p[i].a, h[++M] = p[i].c;
	sort(h+1, h+1+M);
	M = unique(h+1, h+1+M)-h-1;
	for(int i = 0; i <= N; ++i) p[i].update();
	
	for(int i = 1; i <= N; ++i) insert(p[i].a, i);
	for(int i = 1; i <= M; ++i) sort(t[i].begin(), t[i].end(), cmp);
	
	queue <int> q;
	q.push(0);
	while(!q.empty()) {
		int x = q.front(); q.pop();
		for(int i = p[x].c; i; i -= i&-i) 
			while(!t[i].empty() && p[t[i].back()].b <= p[x].d) {
				int y = t[i].back();
				t[i].pop_back();
				if(!dis[y]) dis[y] = dis[x]+1, prev[y] = x, q.push(y);
			}
	}
	
	if(dis[N]) {
		for(int i = N; i; i = prev[i]) ans[++back] = i;
		printf("%d\n", back);
		for(int i = back; i; --i) printf("%d ", ans[i]);
		printf("\n");
	}
	else printf("-1\n");
	
	return 0;
}
