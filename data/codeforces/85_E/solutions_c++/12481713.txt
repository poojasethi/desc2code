#include <stdio.h>
#include <string.h>
#define abs(a) ((a)>0?(a):-(a))
int n,x[5001],y[5001],clr[5001],len;
bool vst[5001];
bool dfs(int k,int c)
{
	int i;
	vst[k]=true;
	clr[k]=c;
	for (i=1;i<=n;i++)
		if (abs(x[k]-x[i])+abs(y[k]-y[i])>len)
		{
			if (i!=k&&vst[i]&&clr[i]==clr[k])
				return false;
			if (!vst[i])
				if (!dfs(i,c^1))
					return false;
		}
	return true;
}
bool check(int l)
{
	int i;
	memset(vst,false,sizeof(vst));
	len=l;
	for (i=1;i<=n;i++)
		if (!vst[i])
			if (!dfs(i,0))
				return false;
	return true;
}
int cal(int l)
{
	int i,cnt=1;
	memset(vst,false,sizeof(vst));
	len=l;
	for (i=1;i<=n;i++)
		if (!vst[i])
		{
			dfs(i,0);
			(cnt<<=1)%=1000000007;
		}
	return cnt;
}
int main()
{
	int i,l=0,r=10000,m;
	scanf("%d",&n);
	for (i=1;i<=n;i++)
		scanf("%d%d",x+i,y+i);
	while (l<r)
	{
		m=(l+r)/2;
		if (check(m))
			r=m;
		else
			l=m+1;
	}
	printf("%d\n%d",l,cal(l));
	return 0;
}
