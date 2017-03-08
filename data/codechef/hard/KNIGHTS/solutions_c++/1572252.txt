#include <bits/stdc++.h>

using namespace std;
#define source 901
#define dest 902
vector<int> g[1000];
int edge[1000][1000] = {0};
int prev[1000];
int cost;
int maxflow()
{
	
	while(1)
	{
		queue<int> q;
		int last,back,v,minm;
		char visited[1000] = {0};
		vector<int>::iterator it;
		q.push(source);
		visited[source] = 1;
		while(!q.empty())
		{
			v = q.front();
			if(v == dest)
			{
				break;
			}
			
			q.pop();
			for(it = g[v].begin(); it!=g[v].end();it++)
			{
				if((!visited[*it]) && (edge[v][*it]!=0))
				{
					q.push(*it);
					visited[*it] = 1;
					prev[*it] = v;
				}
			}		
		}
		if(q.empty())
		{
			return cost;
		}
		back = prev[dest];
		minm = edge[back][dest];
		while(back!=source)
		{
			last = prev[back];
			if(edge[last][back] < minm)
				minm = edge[last][back];
			back = last;
		}
	
		back = prev[dest];
		edge[back][dest] -= minm;
		edge[dest][back] += minm;
		while(back!=source)
		{
			last = prev[back];
			edge[last][back] -= minm;
			edge[back][last] += minm;
			back = last;
		}
		cost+=minm;
	}
	
}

int inbounds(int x,int y,int m,int n)
{
	return (x>=0 && x<m && y>=0 && y<n);
}

int main()
{
	int m,n,i,j,r,k,x,y,dr,error,t;
	char str[40][40];
	int dx[] = {-2,-2,-1,-1,1,1,2,2};
	int dy[] = {-1,1,-2,2,-2,2,-1,1};
	scanf("%d",&t);
	while(t--)
	{
	error = 0;
	for(i = 0;i < 1000;i++)
	{
		g[i].clear();
	}
	memset(edge,0,sizeof(int)*1000*1000);
	scanf("%d %d",&m,&n);
	for(i = 0;i < m;i++)
	{
		scanf("%s",str[i]);
	}
	for(i = 0;i < m;i++)
	{
		
		for(j = 0;j < n;j++)
		{
			if(str[i][j] == '.')
			{
			r = i*n+j;
			if((i+j)&1)
			{
				edge[r][dest] = 1;
				g[r].push_back(dest);
				g[dest].push_back(r);
			}
			else
			{
				edge[source][r] = 1;
				g[r].push_back(source);
				g[source].push_back(r);
			}

			for(k = 0;k < 8;k++)
			{
				x = i+dx[k];
				y = j+dy[k];
				dr = x*n+y;
				if(inbounds(x,y,m,n))
				{
					if(str[x][y]=='.')
					{
					g[r].push_back(dr);
					if(!((i+j)&1))
					{
						edge[r][dr] = 1;
					}
					}
				}
			}
			}
			else
			{
				error++;
			}
		}
	}
	cost = 0;
	printf("%d\n",m*n - error - maxflow());
	}
}
