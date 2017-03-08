#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

const int maxn = 105, inf = 1e9;
int N, M, S, T, K, now, tim;
int d[maxn][maxn], s[maxn], t[maxn], r[maxn], vis[maxn];
bool must[maxn][maxn], found = true;

int main() {
	scanf("%d%d%d%d", &N, &M, &S, &T);
	
	memset(d, 63, sizeof(d));
	memset(r, 63, sizeof(r));
	for(int i = 1; i <= N; ++i) d[i][i] = 0;
	for(int i = 1, u, v; i <= M; ++i)
		scanf("%d%d", &u, &v), d[u][v] = 1;
		
	for(int k = 1; k <= N; ++k)
	for(int i = 1; i <= N; ++i)
	for(int j = 1; j <= N; ++j)
		d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
	
	scanf("%d", &K);
	for(int i = 1; i <= K; ++i) scanf("%d%d", s+i, t+i);
	
	for(int i = 1, x, y; i <= K; ++i) {
		x = s[i], y = t[i];
		for(int j = 1; j <= N; ++j) {
			must[i][j] = (d[x][y] == d[x][j]+d[j][y]);
			for(int k = 1; k <= N; ++k)
				must[i][j] &= (j == k) || (d[x][k] != d[x][j]) || (d[k][y] != d[j][y]);
		}
	}
	
	r[T] = 0;
	while(++now && found) {
		found = false;
		for(int i = 1; i <= K; ++i) if(d[s[i]][t[i]] < inf) {
			for(int j = 1; j <= N; ++j)
			if(must[i][j] && r[j] >= inf) {
				queue <int> q;
				q.push(j), vis[j] = ++tim;
				
				while(!q.empty()) {
					int v = q.front(); q.pop();
					for(int k = 1; k <= N; ++k)
					if(d[v][k] == 1 && r[k] >= now && d[k][t[i]] == d[v][t[i]]-1 && vis[k] != tim)
						q.push(k), vis[k] = tim;
				}
				
				if(vis[t[i]] != tim) r[j] = now, found = true;
			}
		}
	}
	
	printf("%d\n", r[S] < inf ? r[S] : -1);
	return 0;
}
	
