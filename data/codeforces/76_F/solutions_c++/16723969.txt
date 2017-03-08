#include<cstdio>
#include<algorithm>
using namespace std;
pair<long long,long long>a[120000];
long long x1,x2,n,v,m,tmp;
long long b[120000][2];
long long pos[120000];
int main()
{
	scanf("%I64d",&n);
	for (long long i=1;i<=n;i++)
	{
		scanf("%I64d %I64d",&b[i][0],&b[i][1]);
	}
	scanf("%I64d",&v);
	n++;
	for (long long i=1;i<=n;i++)
	{
		a[i].first=b[i][1]*v+b[i][0];
		a[i].second=b[i][1]*v-b[i][0];
	}
	sort(a+1,a+n+1);
	for (long long i=n;i>=1;i--)
	{
		tmp=upper_bound(pos+1,pos+m+1,-a[i].second)-pos;
		if(a[i]==make_pair(0LL,0LL))
		{
			printf("%I64d ",tmp-1);
		}
		else
		{
			pos[tmp]=-a[i].second;
			m=max(tmp,m);
		}
	}printf("%I64d\n",m);
	return 0;
}
