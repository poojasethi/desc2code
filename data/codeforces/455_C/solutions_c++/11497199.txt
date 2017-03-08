#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#define MAXN 300005
using namespace std;
int par[MAXN],diam[MAXN],dep[MAXN],cp;
vector<int> mp[MAXN];
inline int fnd(int k)
{
	return par[k]==k?k:par[k]=fnd(par[k]);
}
inline void uni(int x,int y)
{
	int t1=fnd(x),t2=fnd(y);
	if (t1!=t2)
	{
		par[t1]=t2;
		diam[t2]=max(diam[t2],max(diam[t1],(diam[t2]+1)/2+(diam[t1]+1)/2+1));
	}
}
int dfs(int k,int cp)
{
	int i,o,ans=k,tmp;
	for (i=0;i<mp[k].size();i++)
	{
		o=mp[k][i];
		if (o!=cp)
		{
			dep[o]=dep[k]+1;
			tmp=dfs(o,k);
			if (dep[tmp]>dep[ans])
				ans=tmp;
		}
	}
	return ans;
}
int main()
{
	int n,m,q,i,t1,t2,t3;
	scanf("%d%d%d",&n,&m,&q);
	for (i=1;i<=n;i++)
		par[i]=i;
	for (i=1;i<=m;i++)
	{
		scanf("%d%d",&t1,&t2);
		uni(t1,t2);
		mp[t1].push_back(t2);
		mp[t2].push_back(t1);
	}
	memset(diam,-1,sizeof(diam));
	for (i=1;i<=n;i++)
		if (diam[fnd(i)]==-1)
		{
			t1=dfs(fnd(i),0);
			dep[t1]=0;
			t1=dfs(t1,0);
			diam[fnd(i)]=dep[t1];
		}
	for (i=1;i<=q;i++)
	{
		scanf("%d",&t1);
		if (t1==1)
		{
			scanf("%d",&t2);
			printf("%d\n",diam[fnd(t2)]);
		}
		else
		{
			scanf("%d%d",&t2,&t3);
			uni(t2,t3);
		}
	}
	return 0;
}
