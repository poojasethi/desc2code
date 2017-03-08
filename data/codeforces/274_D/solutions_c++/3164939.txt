#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#define N 200101

using namespace std;

vector<int> tr[N];
vector<int> ans;
struct node{ int x,y; }no[N];

int cmp(node a,node b){ return a.x<b.x; }

int top,v[N],vis[N];

void dfs(int now,int& tag)
{
	if(tag==0) return;
	vis[now]=v[now]=1;
	for(int i=0; i<tr[now].size(); i++)
	{
		int to=tr[now][i];
		if(vis[to]) tag=0;
		if(!v[to])
			dfs(to,tag);
	}
	vis[now]=0;
	ans.push_back(now);
}

void gao(int n)
{
	memset(v,0,sizeof(v));
	memset(vis,0,sizeof(vis));
	ans.clear();
	int tag=1;
	for(int i=0; i<top&&tag; i++)
		if(!v[i])
			dfs(i,tag);
	if(tag==0) 
	{
		puts("-1");
		return;
	}
	for(int i=ans.size()-1; i>=0; i--)
		if(ans[i]<n)
			printf("%d ",ans[i]+1);
	puts("");
}

int main()
{
	int n,m;
	scanf("%d%d",&n,&m);
	top=m;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			int x;
			scanf("%d",&x);
			no[j].x=x,no[j].y=j;
		}
		sort(no,no+m,cmp);
		int pre=-1;
		for(int j=0; j<m; j++)
		{
			if(no[j].x<0) continue;
			if(j>0&&no[j-1].x<no[j].x&&no[j-1].x>=0)
			{
				pre=top;
				top++;
			}
			if(pre>=0)
				tr[pre].push_back(no[j].y);
			tr[no[j].y].push_back(top);
		}
		top++;
	}
	gao(m);
	return 0;
}
