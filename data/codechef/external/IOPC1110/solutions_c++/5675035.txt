# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <queue>
# include <cmath>
# include <cstring>
# include <iostream>
# include <stack>
# include <map>
# include <vector>
# include <utility>
# include <set>
# include <deque>

# define MOD (1000000007)
# define MAXINT 1e9

using namespace std;
typedef long long int ll;

ll d[100005],cost[100005],lr[100005];

void compute(ll n)
{
	stack<ll> s;
	ll i,x;
	for(i=0;i<n;)
	{
		if(s.empty() || cost[s.top()]<cost[i])
			s.push(i++);
		else
		{
			x=s.top();
			s.pop();
			lr[x]=i;
		}
	}
	while(!s.empty())
	{
		x=s.top();
		s.pop();
		lr[x]=-1;
	}
}

int main()
{
	ll test,n,c,fuel,present,x,y,fill,i;
	ll ans;
	scanf("%lld",&test);
	while(test--)
	{
		scanf("%lld%lld",&n,&c);
		d[0]=0;
		for(i=1;i<=n;i++)	scanf("%lld",&d[i]);
		for(i=0;i<n;i++)	scanf("%lld",&cost[i]);
		compute(n);
		fuel=0;
		ans=0;
		for(present=0;present<n;fuel=fuel-d[present+1]+d[present],present++)
		{
			//cout<<fuel<<" ";
			if(lr[present]==-1)
			{
				x=d[n]-d[present];
				//fill=min(c-fuel,x);
				if(fuel>=x)	fill=0;
				else
				{
					if(c>=x)
						fill=x-fuel;
					else
						fill=c-fuel;
				}
				fuel+=fill;
				ans=ans+((ll)fill*cost[present]);
			}
			else
			{
				x=lr[present];
				y=d[x]-d[present];
				if(y<=fuel)
					continue;
				else if(c>=y)
				{
					fill=y-fuel;
					fuel+=fill;
					ans=ans+((ll)fill*cost[present]);
				}
				else
				{
					fill=c-fuel;
					fuel+=fill;
					ans=ans+((ll)fill*cost[present]);
				}
			}
			//cout<<ans<<endl;
		}
		printf("%lld\n",ans);
	}
	return 0;
}