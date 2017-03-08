# include <stdio.h>
# include <vector>
# include <algorithm>

# define MAXN 100009

using namespace std;

int n,q,a,b,root,d;

vector <int> G[MAXN] , T[MAXN];

int deg[MAXN] , pos[MAXN];

void dfs(int cur,int prev,int num)
{
	deg[cur] = deg[prev]+1;
	pos[cur] = num;
	T[num].push_back(0);
	
	for(int h=0; h<(int)G[cur].size(); h++)
	{
		int to = G[cur][h];
		if(prev == to)	continue;
		dfs(to,cur,num);
	}
}

void add(int x,int y,int z)	{for(int h=y; h<(int)T[x].size(); h += h & -h)	T[x][h] += z;}

int query(int x,int y)
{
	int ret = 0;
	
	for(int h=y; h>0; h -= h & -h)	ret += T[x][h];
	
	return ret;
}

int main()
{
	scanf("%d %d",&n,&q);
	
	pos[1] = n+1;
	
	for(int h=0; h<n-1; h++)
	{
		scanf("%d %d",&a,&b);
		G[a].push_back(b);
		G[b].push_back(a);
	}
	
	for(int h=0; h<(int)G[1].size(); h++)	T[h].push_back(0) , dfs(G[1][h],1,h);
	
	T[n].resize(n+9);
	
	for(int h=0; h<q; h++)
	{
		scanf("%d",&a);
		
		if(a)
		{
			scanf("%d",&a);
			
			if(a == 1)	{printf("%d\n",root);continue;}
			
			printf("%d\n",query(n,deg[a])+query(pos[a],deg[a]));
		}
		
		else
		{
			scanf("%d %d %d",&a,&b,&d);
			
			if(deg[a]-d < 1)	root += b;
			
			if(deg[a] <= d)
			{
				int to = d-deg[a];
				add(pos[a],to+1,b);
				add(pos[a],d+deg[a]+1,-b);
				add(n,1,b);
				add(n,to+1,-b);
			}
			
			else
			{
				add(pos[a],deg[a]-d,b);
				add(pos[a],deg[a]+d+1,-b);
			}
		}
	}
}
