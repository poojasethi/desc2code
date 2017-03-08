#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#define rep(i,a,b) for(int i = a; i <= b; i++)
using namespace std;
const int N = 400, M = 3000, inf = 1000000010;
typedef long long LL;

int S, T;
struct edge{
    int to, pre, w;
}e[M * 2];
int cur[N], u[N], l = 1;//l = 1!
void init(){
	for (int i = 2; i <= l; i += 2) e[i].w = e[i ^ 1].w = (e[i].w + e[i ^ 1].w) >> 1;
}
#define ew e[i].w
#define v e[i].to
#define reg(i,a) for(int i = u[a]; i; i = e[i].pre)
#define ceg(i,a) for(int i = cur[a]; i; i = e[i].pre)
void ins(int a, int b, int w){
    e[++l] = (edge){b, u[a], w}, u[a] = l;
}
void insert(int a, int b, int w){//used insert to add an edge instead of using ins!
    ins(a, b, w), ins(b, a, 0);
}
int q[N], h[N], n;
bool bfs(){
    rep(i,1,n) h[i] = -1;
    int l = 0, r = 1; q[h[S] = 0] = S;
    while (l < r){
        int x = q[l++];
        reg(i,x) if (ew && h[v] == -1) h[v] = h[x] + 1, q[r++] = v;
    }
    return h[T] != -1;
}
int dfs(int x, int f){
    if (x == T || f == 0) return f;
    int used = 0, w;
    ceg(i,x)if (ew && h[v] == h[x] + 1){
        w = min(ew, f - used), w = dfs(v, w);
        ew -= w; if (ew) cur[x] = i;
        e[i^1].w += w;
        used += w; if (used == f) break;
    }
    if (!used) h[x] = -1;
    return used;
}
int dinic(){
    int ans = 0;
    while (bfs()){
        rep(i,1,n) cur[i] = u[i];
        ans += dfs(S, inf);
    }
    return ans;
}

int F[N], r[N], bel[N];
void bfsS(){
	int l = 0, r = 1; bel[q[0] = S] = S;
	while (l < r){
		int x = q[l++];
		if (x != S && F[x] == F[S]) F[x] = S;
		reg(i,x) if (ew && bel[v] != S) bel[v] = S, q[r++] = v;
	}
}

void build(){
	rep(i,2,n) F[i] = 1;
	rep(i,2,n){
		S = i, T = F[i];
		init();
		r[i] = dinic();
		bfsS();
	}
}

int f[N];
typedef pair<int, int> edg;
#define mp(a,b) make_pair(a,b)
edg R[N];

int find(int x){
	return x == f[x] ? x : find(f[x]);
}

#define pb(a) push_back(a)
vector<int> path[N];
typedef vector<int>::iterator vit;
void merge(int a, int b){
	int fa = find(a), fb = find(b);
	if ((fa ^ fb) >> 2 & 1) swap(fa,fb);
	f[fb] = fa;
	for (vit it = path[fb].begin(); it != path[fb].end(); it++)
		path[fa].pb(*it);
}

void work(){
	LL ans = 0;
	rep(i,1,n) f[i] = i;
	rep(i,2,n) ans += r[i];
	rep(i,2,n) R[i - 1] = mp(-r[i], i);
	sort(R + 1, R + n);
	rep(i,1,n) path[i].pb(i);
	rep(i,1,n - 1){
		int x = R[i].second;
		merge(x, F[x]);
	}
	int rt = find(1);
	cout <<ans<<endl;
	for(vit it = path[rt].begin(); it != path[rt].end(); it++)
		printf("%d ",*it);
	printf("\n");
}

int main(){
	int m; scanf("%d%d",&n,&m);
	rep(i,1,m){
		int a, b, c;
		scanf("%d%d%d",&a,&b,&c);
		ins(a,b,c), ins(b,a,c);
	}
	build();
	work();
	return 0;
}