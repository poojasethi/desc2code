#include <cstdio>
#include <algorithm>

using namespace std;
typedef long long ll;

ll arr[2500];

int main()
{
	
	ll n,h;
	scanf("%lld%lld",&n,&h);
	arr[0]=h;
	ll count=1,mod=1000000007;
	for(ll i=1;i<=n+1;i++)
	{
		if(i<=n)
			scanf("%lld",&arr[i]);
		else
			arr[i]=h;

		if(arr[i]-arr[i-1]>(ll)1 || arr[i-1]-arr[i]>(ll)1)
		{
			printf("0\n");
			return 0;
		}
		if(arr[i]!=arr[i-1]-1)
			count=count*(h-arr[i]+(ll)1)%mod;
	}	
	printf("%lld\n",count);
	return 0;
}
