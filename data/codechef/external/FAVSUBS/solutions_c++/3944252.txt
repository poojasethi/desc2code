#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;
typedef long long ll;

ll min(ll a,ll b)
{
	return a<b?a:b;
}

ll a[1000006];
ll workspace[10003];
map<ll,ll> m;

void update(ll node,ll l,ll r,ll q,ll v)
{
	if(q<l || q>r)	return;
	if(l==r && l==q)	{
		workspace[node]=v;
		return;
	}
	update(node<<1,l,(l+r)>>1,q,v);
	update((node<<1)+1,((l+r)>>1)+1,r,q,v);
	workspace[node]=min(workspace[node<<1],workspace[(node<<1)+1]);
	return;
}

int main()
{
	ll test,n,k,i,q,ans;
	scanf("%lld",&test);
	while(test--)
	{
		m.clear();
		ans=0;
		scanf("%lld",&n);
		for(i=0;i<n;i++)	scanf("%lld",&a[i]);
		scanf("%lld",&k);
		for(i=0;i<k;i++)
		{
			scanf("%lld",&q);
			m[q]=i;
		}
		for(i=0;i<=10000;i++)	workspace[i]=-1;
		for(i=0;i<n;i++)
		{
			if(m.find(a[i])!=m.end())
				update(1,0,k-1,m[a[i]],i);
			q=workspace[1];
			if(q!=-1)
				ans+=q+1;
				//printf("**%lld %lld\n",q+1,i);
		}
		printf("%lld\n",ans);
	}
	return 0;
}