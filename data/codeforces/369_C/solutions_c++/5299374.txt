# include <stdio.h>
# include <vector>
# include <algorithm>

# define MAXN 100009

using namespace std;

int n, ans;
vector< pair<int,int> > G[MAXN];
int vis[MAXN], D[MAXN];

void dfs(int node,int par,int fix)
{
	for(int h=0; h<(int)G[node].size(); h++)
	{
		int to = G[node][h].first;
		
		if(to == par)	continue;
		
		dfs(to, node, G[node][h].second);
		
		vis[node] += vis[to];
	}
	
	if(!vis[node]  &&  fix)	D[ans++] = node, vis[node] = 1;
}

int main()
{
	scanf("%d",&n);
	
	for(int h=0; h<n-1; h++)
	{
		int a, b, c;
		
		scanf("%d %d %d",&a,&b,&c);
		c--;
		G[a].push_back(make_pair(b, c));
		G[b].push_back(make_pair(a, c));
	}
	
	dfs(1, -1, 0);
	
	printf("%d\n",ans);
	
	for(int h=0; h<ans; h++)	printf("%d ",D[h]);
}
