#include <bits/stdc++.h>

using namespace std;

#define ll long long int

int main()
{
	int n;
	cin>>n;
	vector<ll> vec;
	vec.resize(n);
	for(ll i=0;i<n;i++)
	{
		cin>>vec[i];
	}
	ll count,ans=0,var=1;
	for(ll i=0;i<32;i++)
	{
		count=0;
		for(ll j=0;j<n;j++)
		{
			count+=(vec[j]&0x1);
			vec[j]=vec[j]>>1;
		}
		ans+=(count*(count-1)*var)/2;
		//cout<<count<<" "<<(count*(count-1)*var)<<endl;
		var*=2;
	}
	cout<<ans<<endl;
}