#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stack>
#include <map>
#include <vector>
#define mod (1000000009)

using namespace std;
typedef long long int ll;

ll c[8000006];
ll a[2000000];

int main()
{
	ll test,ma,n,p,m,i;
	ll ans,x;
	scanf("%lld",&test);
	while(test--)
	{
		scanf("%lld",&n);
		scanf("%lld",&p);
		m=100000000;
		for(i=1;i<n;i++)
		{
			scanf("%lld",&x);
			a[i-1]=p-x;
			m=min(m,a[i-1]);
			p=x;
		}
		ma=0;
		for(i=0;i<n-1;i++)
		{
			a[i]-=m;
			c[a[i]]=0;
		}
		ans=1;
		for(i=0;i<n-1;i++)
		{
			x=c[a[i]];
			c[a[i]]=ans;
			ans=(ans+ans-x+2*mod);
			ans=ans%mod;
		}
		printf("%lld\n",ans-1);
	}
	return 0;
}