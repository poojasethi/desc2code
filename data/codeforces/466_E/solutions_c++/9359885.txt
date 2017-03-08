#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <vector>
using namespace std;

int col[100005][2], par[100005];
int t[100005][2];
int vis[100005];
vector<vector<int> > adj;
vector<int> P, Q;
int N, M, K;
int ctr;

void init(){
	for(int i=0;i<=N;++i) par[i] = i;
}

int find(int u){
	return (par[u] == u ? u : (par[u] = find(par[u])));
}

void dfs(int u){
	vis[u] = 1;
	t[u][0] = ctr++;
	for(int i=0;i<adj[u].size();++i){
		int v = adj[u][i];
		if(vis[v])continue;
		dfs(v);
	}
	t[u][1] = ctr++;
}

int main(){
	int type,u,v;
	K = 1;
	scanf("%d %d", &N, &M);
	adj = vector<vector<int> > (N+3);
	init();
	for(int i=0;i<M;++i){
		scanf("%d", &type);
		if(type == 1){
			scanf("%d %d", &u, &v);
			par[find(u)] = v;
			adj[u].push_back(v);
			adj[v].push_back(u);
		} else if(type==2){
			scanf("%d", &u);
			col[K][0] = u;
			col[K][1] = find(u);
			++K;
		} else if(type==3){
			scanf("%d %d", &u,&v);
			P.push_back(u);
			Q.push_back(v);
		}
	}
	ctr = 0;
	for(int i=1;i<=N;++i){
		if(par[i]==i){
			dfs(i);
		}
	}
	for(int i=0;i<P.size();++i){
		u = col[Q[i]][0];
		v = col[Q[i]][1];
		if(t[u][0] >= t[P[i]][0] && t[P[i]][1] >= t[u][1] &&
		   t[v][0] <= t[P[i]][0] && t[P[i]][1] <= t[v][1]){
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}