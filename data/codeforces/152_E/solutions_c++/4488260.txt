#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
using namespace std;

int dp[410][130],vis[410][130];
int a[110][110],sta[110][110];
pair<int,int>pre[410][130];

int n,m;
queue<pair<int,int> >q;

int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};
int bfs(int N)
{
	int i,j,k;

	memset(dp,-1,sizeof(dp));
	memset(vis,0,sizeof(vis));

	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
		{
			q.push(make_pair(i*m+i+j,sta[i][j]));
			vis[i*m+i+j][sta[i][j]]=1;
			dp[i*m+i+j][sta[i][j]]=a[i][j];
			pre[i*m+i+j][sta[i][j]].first=-1;
			pre[i*m+i+j][sta[i][j]].second=-1;

			if(sta[i][j])
			{
				q.push(make_pair(i*m+i+j,0));
				dp[i*m+i+j][0]=a[i][j];
				vis[i*m+i+j][0]=1;
				pre[i*m+i+j][0].first=-1;
				pre[i*m+i+j][0].second=-1;
			}
		}
	int x,y,xx,yy,s,ss,u,v;

	while(!q.empty())
	{
		u=q.front().first;
		x=q.front().first/(m+1);
		y=q.front().first%(m+1);
		s=q.front().second;

		q.pop();
		vis[u][s]=0;

		for(i=0;i<4;i++)
		{
			xx=x+dx[i];
			yy=y+dy[i];
			v=xx*m+xx+yy;
			if(xx>=1&&xx<=n&&yy>=1&&yy<=m)
			{
				ss=(s|sta[xx][yy]);
				if(dp[v][ss]<0||dp[v][ss]>dp[u][s]+a[xx][yy])
				{
					dp[v][ss]=dp[u][s]+a[xx][yy];
					pre[v][ss].first=u;
					pre[v][ss].second=s;

					if(!vis[v][ss])
						vis[v][ss]=1,q.push(make_pair(v,ss));
				}
			}
		}
		int bu=(1<<N)-1-s;

		for(i=bu;i;i=(i-1)&bu)if(dp[u][i]>=0)
		{
			ss=(s|i);
			xx=x,yy=y;
			v=xx*m+xx+yy;
			if(xx>=1&&xx<=n&&yy>=1&&yy<=m)
			{
				if(dp[v][ss]<0||dp[v][ss]>dp[u][s]+dp[u][i]-a[xx][yy])
				{
					dp[v][ss]=dp[u][s]+dp[u][i]-a[xx][yy];
					pre[v][ss].first=u;
					pre[v][ss].second=s;
					if(!vis[v][ss])
						vis[v][ss]=1,q.push(make_pair(v,ss));
				}
			}
		}
	}
	int ans=210000;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
		{
			u=i*m+i+j;
			if(dp[u][(1<<N)-1]>=0)
				ans=min(ans,dp[u][(1<<N)-1]);
		}
	return ans;
}
int gao[110][110];
void dfs(int u,int s)
{
	if(u<0)
		return;
	int v,ss;
	gao[u/(m+1)][u%(m+1)]=1;
	v=pre[u][s].first;
	ss=pre[u][s].second;

	if(v==u)
		dfs(u,s-ss),dfs(u,ss);
	else
		dfs(v,ss);
}
int main()
{
	int k,i,j,x,y;

	scanf("%d%d%d",&n,&m,&k);
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
		scanf("%d",&a[i][j]);
	for(i=0;i<k;i++)
	{
		scanf("%d%d",&x,&y);
		sta[x][y]=(1<<i);
	}
	int t;
	printf("%d\n",t=bfs(k));
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
		{
			x=i*m+i+j;
			if(dp[x][(1<<k)-1]==t)
			{
				dfs(x,(1<<k)-1);
				for(i=1;i<=n;i++)
				{
					for(j=1;j<=m;j++)if(gao[i][j])
						printf("X");
					else
						printf(".");
					puts("");
				}
				return 0;
			}
		}
}