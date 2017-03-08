# include <stdio.h>
# include <algorithm>
# include <vector>

# define MAXN 100009
# define ma(x,y) (x>y ? x : y)

using namespace std;

vector < pair <int,int> > G[MAXN];

int n,a,b,c;

long long k,l;

int D[MAXN];

void dfs(int cur,int prev)
{
	l = ma(D[cur],l);
	
	for(int h=0; h<(int)G[cur].size(); h++)
	{
		int to = G[cur][h].first;
		
		if(to == prev)	continue;
		
		D[to] = D[cur]+G[cur][h].second;
		
		dfs(to,cur);
	}
	
}

int main()
{
	scanf("%d",&n);
	
	for(int h=0; h<n-1; h++)
	{
		scanf("%d %d %d",&a,&b,&c);
		G[a].push_back(make_pair(b,c));
		G[b].push_back(make_pair(a,c));
		k += 2*c;
	}
	
	dfs(1,-1);
	
	printf("%I64d",k-l);
}
