#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAXN=100005;
const int INF=100000000;
int head[MAXN],E;
struct Edge
{
	int v,c,next;
}edge[MAXN<<1];
int llimit,rlimit;
int xx,yy;
bool vis[MAXN];
int s[MAXN],f[MAXN];
int mid,ans;
int to[MAXN],tot;
int w[MAXN];
int max_l;
inline int max(int a,int b)
{
	return a>b?a:b;
}
bool cmp(int a,int b)
{
	return s[a]<s[b];
}
void add_edge(int u,int v,int c)
{
	edge[E].v=v;
	edge[E].c=c;
	edge[E].next=head[u];
	head[u]=E++;
}
int root(int u,int fa,int size)
{
	int i,ret=-1;
	s[u]=1;
	f[u]=0;
	for(i=head[u];i!=-1;i=edge[i].next)
	{
		int v=edge[i].v;
		if(v==fa||vis[v])
			continue;
		int x=root(v,u,size);
		s[u]+=s[v];
		f[u]=max(f[u],s[v]);
		if(ret==-1||f[x]<f[ret])
			ret=x;
	}
	f[u]=max(f[u],size-s[u]);
	if(ret==-1||f[u]<f[ret])
		ret=u;
	return ret;
}
int ff[MAXN];
int q[MAXN];
int px[MAXN],py[MAXN];
void dfs(int u,int fa,int dep,int sum)
{
	if(sum>f[dep])
	{
		f[dep]=sum;
		py[dep]=u;
	}
	int i;
	for(i=head[u];i!=-1;i=edge[i].next)
	{
		int v=edge[i].v;
		if(v==fa||vis[v])
			continue;
		if(edge[i].c>=mid)
			dfs(v,u,dep+1,sum+1);
		else
			dfs(v,u,dep+1,sum-1);
	}
}
bool check(int u)
{
	int i,j,k=0;
	px[0]=u;
	for(i=1;i<=s[to[tot-1]];i++)
		ff[i]=-INF;
	for(i=0;i<tot;i++)
	{
		int v=to[i];
		for(j=1;j<=s[v];j++)
			f[j]=-INF;
		if(w[v]>=mid)
			dfs(v,u,1,1);
		else
			dfs(v,u,1,-1);
		int qh=1,qt=0;
		for(j=1;j<=s[v];j++)
		{
			if(f[j]==-INF)
				break;
			while(k>=0&&j+k>=llimit)
			{
				while(qh<=qt&&ff[q[qt]]<ff[k])
					qt--;
				q[++qt]=k;
				k--;
			}
			while(qh<=qt&&q[qh]+j>rlimit)
				qh++;
			if(qh<=qt&&ff[q[qh]]+f[j]>=0)
			{
				xx=px[q[qh]];
				yy=py[j];
				ans=mid;
				return true;
			}
		}
		for(k=1;k<j;k++)
			if(f[k]>ff[k])
				ff[k]=f[k],px[k]=py[k];
		k--;
	}
	return false;
}
void gao(int u,int size)
{
	int i;
	tot=0;
	for(i=head[u];i!=-1;i=edge[i].next)
	{
		int v=edge[i].v;
		if(vis[v])
			continue;
		if(s[v]>s[u])
			s[v]=size-s[u];
		to[tot++]=v;
		w[v]=edge[i].c;
	}
	if(!tot)
		return ;
	sort(to,to+tot,cmp);
	int l=ans+1,r=max_l;
	mid=l;
	if(!check(u))
		return ;
	while(l<=r)
	{
		mid=(l+r)>>1;
		if(check(u))
			l=mid+1;
		else
			r=mid-1;
	}
}
void solve(int u,int size)
{
	int i,x=root(u,0,size);
	vis[x]=1;
	gao(x,size);
	for(i=head[x];i!=-1;i=edge[i].next)
	{
		int v=edge[i].v;
		if(vis[v])
			continue;
		solve(v,s[v]);
	}
}
int main()
{
	int n,i,j;
	scanf("%d%d%d",&n,&llimit,&rlimit);
	memset(head,-1,sizeof(head));
	E=0;
	int x,y,z;
	for(i=1;i<n;i++)
	{
		scanf("%d%d%d",&x,&y,&z);
		add_edge(x,y,z);
		add_edge(y,x,z);
		max_l=max(max_l,z);
	}
	ans=-1;
	solve(1,n);
	printf("%d %d\n",xx,yy);
	return 0;
}