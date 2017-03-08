#include <cstdio>
#include <cstring>
#include <vector>
#define N 100011
#define pii pair<int,int>

using namespace std;

struct edge{ int f,t,i;
	edge(int x,int y,int z){ f=x,t=y,i=z; }
	edge(){;}
};

vector<edge> e;
vector<int> li[N];
vector<pii> tr[N];
vector<int> ans;
int dfn[N],id[N],low[N],top,st[N],vis[N],ID,TI,pre[N],in[N];

void tar(int now)
{
	dfn[now]=low[now]=TI++;
	st[++top]=now;
	vis[now]=1;
	for(int i=0; i<li[now].size(); i++)
	{
		int to=li[now][i];
		if(!dfn[to])
		{
			tar(to);
			low[now]=min(low[now],low[to]);
		}
		else if(vis[to])
			low[now]=min(low[now],dfn[to]);
	}
	if(low[now]==dfn[now])
	{
		for(; top>=0; )
		{
			int x=st[top--];
			id[x]=ID;
			vis[x]=0;
			if(x==now)
				break;
		}
		ID++;
	}
}

void dfs(int now)
{
	vis[now]=1;
	for(int i=0; i<tr[now].size(); i++)
	{
		int to=tr[now][i].first,id=tr[now][i].second;
		if(!vis[to])
		{
			dfs(to);
			if(id>0)
				ans.push_back(id);
		}
	}
}

int main()
{
	int n,m;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	while(scanf("%d%d",&n,&m)+1)
	{
		e.clear();
		for(int i=0; i<n; i++)
		{
			li[i].clear();
			tr[i].clear();
		}
		for(int i=0; i<m; i++)
		{
			int x,y,z;
			scanf("%d%d%d",&x,&y,&z);
			y--,x--;
			if(z==0)
				li[x].push_back(y);
			else
				e.push_back(edge(x,y,i));
		}
		TI=1;
		top=0;
		ID=0;
		memset(dfn,0,sizeof(dfn));
		memset(vis,0,sizeof(vis));
		for(int i=0; i<n; i++)
			if(!dfn[i])
				tar(i);
		memset(pre,0,sizeof(pre));
		memset(in,0,sizeof(in));
		for(int i=0; i<n; i++)
			for(int j=0; j<li[i].size(); j++)
			{
				int to=li[i][j];
				if(id[to]==id[i]) continue;
				in[id[to]]++;
				tr[id[i]].push_back(make_pair(id[to],0));
			}
		for(int i=0; i<e.size(); i++)
		{
			int f=id[e[i].f],t=id[e[i].t];
			if(f!=t&&in[t]==0&&t!=id[0])
			{
				tr[f].push_back(make_pair(t,e[i].i+1));
			}
		}
		memset(vis,0,sizeof(vis));
		ans.clear();
		dfs(id[0]);
		int ret=1;
		for(int i=0; i<ID; i++)
			if(!vis[i])
				ret=0;
		if(ret==0)
			puts("-1");
		else
		{
			printf("%d\n",ans.size());
			for(int i=0; i<ans.size(); i++)
			{
				if(i>0) printf(" ");
				printf("%d",ans[i]);
			}
			puts("");
		}
	}
	return 0;
}
