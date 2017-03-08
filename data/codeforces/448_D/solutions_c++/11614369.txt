#include <stdio.h>
#define min(a,b) (a>b?b:a)
int main()
{
	long long n,m,i,k,l=0,r,md,cnt;
	scanf("%I64d%I64d%I64d",&n,&m,&k);
	r=n*m;
	while (r>l+1)
	{
		md=(l+r)/2;
		cnt=0;
		for (i=1;i<=n;i++)
			cnt+=min(m,md/i);
		if (cnt>=k)
			r=md;
		else
			l=md;
	}
	printf("%I64d",r);
	return 0;
}
