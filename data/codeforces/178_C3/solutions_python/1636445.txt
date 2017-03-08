#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
using namespace std;
const int N=200012;
map<int,int> M;
int n,m,h,fa[N],st[N],en[N],pos[N],tot,top,a[N],c[N],past[N],x,y;
long long ans;
inline void add(int k,int delta)
{
	for(;k<=top;k+=k&(-k))
		c[k]+=delta;
}
inline int sum(int k)
{
	int ans=0;
	for(;k;k-=k&(-k))
		ans+=c[k];
	return ans;
}
inline void work(int x)
{
	fa[x]=tot;pos[x]=top;past[top]=x;
	for(x=(x+m)%h;fa[x]==0;x=(x+m)%h) 
	{
		fa[x]=tot;
		pos[x]=++top;
		past[top]=x;
	}
}
int find(int now)
{
	int l=pos[now],r=en[fa[now]],res=-1,s=sum(l-1),u=l-1;
	while (l<=r)
	{
		int mid=(l+r)>>1;
		if (sum(mid)-s<mid-u) res=mid,r=mid-1;else l=mid+1;
	}
	if (res!=-1)
	{
		ans+=res-u-1;
		add(res,1);
		return res;
	}
	l=st[fa[now]];r=pos[now]-1;s=sum(l-1);u=l-1;
	while (l<=r)
	{
		int mid=(l+r)>>1;
		if (sum(mid)-s<mid-u) res=mid,r=mid-1;else l=mid+1;
	}
	ans+=res-u+en[fa[now]]-pos[now];
	add(res,1);
	return res;
}
int main()
{
	scanf("%d%d%d",&h,&m,&n);
	for(int i=0;i<h;++i)
		if (fa[i]==0) st[++tot]=++top,work(i),en[tot]=top;
	for(int i=1;i<=n;++i)
	{
		getchar();char ch=getchar();
		if (ch=='+')
		{
			scanf("%d%d",&x,&y);
			M[x]=find(y);
		}
		else scanf("%d",&x),add(M[x],-1);
	}		
	printf("%I64d\n",ans);
}