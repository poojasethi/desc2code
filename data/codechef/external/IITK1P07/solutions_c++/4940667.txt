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

ll mod;

ll mul(ll a, ll b)
{
	ll ans=0,t=a%mod;
	while(b>0)
	{
		if(b%2)
			ans=(ans+t)%mod;
		t=(t*2)%mod;
		b/=2;
	}
	return ans;
}

ll mulmod(ll a, ll b)
{
   a %= mod;
   b %= mod;
   long double res = a;
   res *= b;
   ll c = (ll)(res / mod);
   a *= b;
   a -= c * mod;
   a %= mod;
   if (a < 0) a += mod;
   return a;
}

ll power(ll a,ll b)
{
	if(b==0)	return 1;
	ll t=power(a,b>>1);
	t=mulmod(t,t);
	if(b&1)
		t=mulmod(t,a);
	return t;
}

ll solve(ll x,ll m)
{
	if(m==0)	return 1;
	if(m%2==0)
	{
		ll t1=solve(x,m>>1);
		ll t=(t1-1);
		if(t<0)	t+=mod;
		ll t2=mulmod(power(x,m>>1),t);
		t1=(t1+t2)%mod;
		return t1;
	}
	else
	{
		ll t1=solve(x,m>>1);
		ll t2=mulmod(power(x,m-(m>>1)),t1);
		t1=(t1+t2)%mod;
		return t1;
	}
}

int main()
{
	ll test,x,m,ans;
	cin>>test;
	while(test--)
	{
		cin>>x>>m>>mod;
		ans=solve(x,m);
		cout<<ans<<endl;
	}

}