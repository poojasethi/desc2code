#include <iostream>
#include <algorithm>
typedef long long LL;
using namespace std;
pair<LL,LL> p[100001];
int main()
{
	LL n,r,avg,i,ttl;
	cin>>n>>r>>avg;
	ttl=n*avg;
	for (i=1;i<=n;i++)
	{
		cin>>p[i].second>>p[i].first;
		ttl-=p[i].second;
	}
	sort(p+1,p+n+1);
	LL res=0;
	LL have,need;
	for (i=1;i<=n;i++)
	{
		if (ttl<=0) break;
		have=r-p[i].second;
		need=min(ttl,have);
		res+=need*p[i].first;
		ttl-=need;
	}
	cout<<res;
	return 0;
}
