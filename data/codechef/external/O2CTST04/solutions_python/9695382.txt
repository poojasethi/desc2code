#include<bits/stdc++.h>
using namespace std;
#include<vector>
#define get(a) scanf("%lld",&a)
#define put(a) printf("%lld",a)
#define ll long long
#define pb push_back
#include<string>
#define FOR(i,a,b) for(ll i=a;i<b;i++)
#define BOOST ios_base::sync_with_stdio(false); cin.tie(NULL)

ll max(vector<ll> ,ll,ll);

int main()
{
	ll n,i,s,a,t,k,j,count,sum;//hes going to input it ONLY in the way he has shown where even the space and enter keys are crutial
	get(t);
	while(t--)
	{
		get(n);
		if(n==1)
		{
			cout<<1<<endl;
			continue;
		}
		vector<ll> v;
		for(i=0;i<n;i++)
		{
			get(a);
			v.pb(a);
		}//learning from talas habits
		sort(v.begin(),v.end());
		i=0;j=1;
		count=0;
		sum=0;
		while(sum!=(-n))
		{
		  	if(v[i]<v[j] && v[i]>0 &&v[j]>0)
		  	{
		  		v[i]=-1;
		  		sum-=1;
		  		i=j;
		  		j++;
		  		if(j==v.size())
		  		{
		  			v[i]=-1;
		  			sum-=1;
		  			i=0;j=1;
		  			count++;
		  			continue;
		  		}
		  		
		  	}
		  	if(v[i]==v[j])
		  	{
		  		j++;
		  		if(j==v.size())
		  		{
		  			v[i]=-1;
		  			sum-=1;
		  			i=0;j=1;
		  			count++;
		  				continue;
		  		}
		  		
		  	}
		  	if(v[i]<0)
		  	{
		  		i++;
		  		//j++;
		  	}
		  	if(v[j]<0)
		  	{
		  		j++;
		  		if(j==v.size())
		  		{
		  			v[i]=-1;
		  			sum-=1;
		  			i=0;j=1;
		  			count++;
		  				continue;
		  		}
		  	}
		  	//cout<<i<<j<<sum<<-n<<endl;
		}
		cout<<count<<endl;
	
		
	}
}

