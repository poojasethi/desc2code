#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stack>
#include <map>

using namespace std;
typedef long long int ll;
ll a[1000000],b[1000000];
pair<ll,ll> places[34];
int main()
{
	ll test,n,i,j,ans,q;
	scanf("%lld",&test);
	while(test--)
	{
		scanf("%lld",&n);
		for(i=0;i<=32;i++)	places[i].first=places[i].second=0;
		for(i=1;i<=n;i++)	scanf("%lld",&a[i]);
		b[0]=0;
		for(i=1;i<=n;i++)	b[i]=b[i-1]^a[i];
		//for(i=0;i<=n;i++)	printf("%lld\n",b[i]);
		for(i=0;i<=n;i++)
		{
			for(j=0;j<=31;j++)
			{
				if(b[i]&(1<<j))	places[j].first++;
				else			places[j].second++;
			}
		}
		//for(i=0;i<=32;i++)	printf("%lld %lld\n",places[i].first,places[i].second);
		ans=0;
		for(i=0;i<=32;i++)
		{
			q=(places[i].first*places[i].second);
			//printf("%lld\n",q);
			ans=ans+q*(1<<i);
			//printf("%lld\n",q);
		}
		printf("%lld\n",ans);
	}
	return 0;
}