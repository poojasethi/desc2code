#include <bits/stdc++.h>

using namespace std;

const int MaxN=5E5+10;
bool mark[MaxN];
int dist[MaxN],dp[MaxN];
vector <int> adj[MaxN];
vector <int> leaf;

bool cmp(int a,int b){
	return a>b;
}

void dfs(int v){
	mark[v]=true;
	if (adj[v].size()==1)
		leaf.push_back(dist[v]);
	for (int i=0;i<adj[v].size();++i){
		int u=adj[v][i];
		if (mark[u]==false){
			dist[u]=dist[v]+1;
			dfs(u);
		}
	}
}

int main(){
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i=0;i<n-1;++i){
		int u,v;
		cin >> u >> v;
		--u;
		--v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	int ans=0;
	mark[0]=true;
	for (int i=0;i<adj[0].size();++i){
		int u=adj[0][i];
		dfs(u);
		sort(leaf.begin(),leaf.end(),cmp);
		int cnt=1;
		for(int j=0;j<leaf.size();++j)
			ans=max(ans,leaf[j]+cnt++);
		leaf.clear();
	}
	cout << ans;
}