#include <stdio.h>
#include <queue>
using namespace std;
long long sr[1001],sc[1001],hr[1000001],hc[1000001];
priority_queue<long long> qr,qc;
int main()
{
	int n,m,k,p,i,j,c;
	long long tmp,f,ans=-100000000000000000;
	scanf("%d%d%d%d",&n,&m,&k,&p);
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++)
		{
			scanf("%d",&c);
			sr[i]+=c;
			sc[j]+=c;
		}
	for (i=1;i<=n;i++)
		qr.push(sr[i]);
	for (i=1;i<=m;i++)
		qc.push(sc[i]);
	for (i=1;i<=k;i++)
	{
		f=qr.top();
		qr.pop();
		qr.push(f-m*p);
		hr[i]=hr[i-1]+f;
		f=qc.top();
		qc.pop();
		qc.push(f-n*p);
		hc[i]=hc[i-1]+f;
	}
	for (i=0;i<=k;i++)
		if ((tmp=hr[i]+hc[k-i]-((long long)i)*(k-i)*p)>ans)
			ans=tmp;
	printf("%I64d",ans);
	return 0;
}
