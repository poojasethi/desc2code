#include <stdio.h>
#define max(a,b) ((a)>(b)?(a):(b))
int h[100001],n,m,w;
long long j[100001];
bool check(long long mh)
{
	int i;
	long long cur=0,cnt=0;
	for (i=1;i<=n;i++)
	{
		if (i-w>0)
			cur-=j[i-w];
		long long jc=max(mh-h[i]-cur,0LL);
		j[i]=jc;
		cur+=jc;
		cnt+=jc;
		if (cnt>m)
			return false;
	}
	return true;
}
int main()
{
	long long l,r,md;
	int i;
	scanf("%d%d%d",&n,&m,&w);
	for (i=1;i<=n;i++)
		scanf("%d",h+i);
	l=0;
	r=10000000000000000;
	while (l+1<r)
	{
		md=(l+r)/2;
		if (check(md))
			l=md;
		else
			r=md;
	}
	printf("%I64d",l);
	return 0;
}
