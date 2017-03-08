#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
int a[400010],cnt[400010],f1[400010],f2[400010],g1[400010],g2[400010],
	h[400010],ans[400010],i,n,m,now,t;
struct abc{int a,b,id;}q[400010];
bool comp(abc x,abc y){return x.a<y.a;}
int find1(int x)
{
	if (x>a[t]) return t+1;
	int l=1,r=t,mid;
	for (;l<=r;)
	{
		mid=(l+r)>>1;
		if (a[mid-1]<x && x<=a[mid]) return mid;
		if (a[mid]<x) l=mid+1;else r=mid-1;
	}
	return 0;
}
int find2(int x)
{
	if (x<a[t]) return t+1;
	int l=1,r=t,mid;
	for (;l<=r;)
	{
		mid=(l+r)>>1;
		if (a[mid-1]>x && x>=a[mid]) return mid;
		if (a[mid]>x) l=mid+1;else r=mid-1;
	}
	return 0;
}
int main()
{
		scanf("%d%d\n",&n,&m);
		for (i=1;i<=n;++i) scanf("%d",&h[i]);scanf("\n");
		for (i=1;i<=m;++i) scanf("%d%d\n",&q[i].a,&q[i].b),q[i].id=i;
		sort(q+1,q+m+1,comp);
		a[t=0]=0;now=1;
		for (i=1;i<=n;++i)
		{
			for (;q[now].a==i;now++) g1[q[now].id]=find1(q[now].b);
			a[f1[i]=find1(h[i])]=h[i];
			if (f1[i]>t) t=f1[i];
		}
		a[t=0]=1e9+1;now=m;
		for (i=n;i;i--)
		{
			for (;q[now].a==i;now--) g2[q[now].id]=find2(q[now].b);
			a[f2[i]=find2(h[i])]=h[i];
			if (f2[i]>t) t=f2[i];
		}
		for (i=1;i<=n;++i)
			if (f1[i]+f2[i]==t+1) cnt[f1[i]]++;
		for (i=1;i<=m;++i)
		{
			now=q[i].id;
			if (f1[q[i].a]+f2[q[i].a]==t+1 && cnt[f1[q[i].a]]==1) ans[now]=t-1;
				else ans[now]=t;
			ans[now]=max(ans[now],g1[now]+g2[now]-1);
		}
		for (i=1;i<=m;++i) printf("%d\n",ans[i]);
}