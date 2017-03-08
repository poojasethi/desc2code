#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=20;
const int inf=1e9;
int dp[maxn][maxn][maxn];
int vis[maxn][maxn][maxn];
int path[maxn][maxn][maxn];
int n,a,b;
int h[maxn];
int dfs(int i,int cur,int pre)
{
	cur=cur<0?0:cur;
	pre=pre<0?0:pre;
	if(i==n)
	{
		if(cur==0) return 0;
		else return inf;
	}
	if(vis[i][cur][pre]) return dp[i][cur][pre];
	vis[i][cur][pre]=1;
	int &ans=dp[i][cur][pre];
	ans=inf;
	int lb=(pre+b-1)/b,hb=max(lb,max((cur+a-1)/a,(h[i+1]+b)/b));
	int p;
	for(int j=lb;j<=hb;j++)
	{
		int tmp=j+dfs(i+1,h[i+1]+1-j*b,cur-j*a);
		if(ans>tmp)
		{
			ans=tmp;
			path[i][cur][pre]=j;
		}
	}
	return ans;
}
void print(int i,int cur,int pre)
{
	cur=cur<0?0:cur;
	pre=pre<0?0:pre;
	if(i==n) return;
	int tmp=path[i][cur][pre],cnt=tmp;
	while(cnt--) printf("%d ",i);
	print(i+1,h[i+1]+1-tmp*b,cur-tmp*a);
}
int main()
{
	cin>>n>>a>>b;
	for(int i=1;i<=n;i++) cin>>h[i];
	memset(vis,0,sizeof(vis));
	int ans=dfs(2,h[2]+1,h[1]+1);
	cout<<ans<<"\n";
	print(2,h[2]+1,h[1]+1);
	puts("");
	return 0;
}
