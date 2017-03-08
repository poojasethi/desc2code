#include <bits/stdc++.h>

using namespace std;

#define ll long long int

vector<ll> wegts,cst;
ll n,k;

ll getans(int x)
{
	ll tempwt=0,tempcst=0;
	for(int i=0;i<n;i++)
	{
		tempcst+=((ll)(x&0x1)*cst[i]);
		tempwt+=((ll)(x&0x1)*wegts[i]);
		x=x>>1;
	}
	if(tempcst<=k)return tempwt;
	else return 0;
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>k;
		wegts.resize(n);
		cst.resize(n);
		for(int j=0;j<n;j++)
		{
			cin>>cst[j]>>wegts[j];
		}
		ll ans=0;
		for(int j=0;j<1024;j++)
		{
			ans=max(ans,getans(j));
		}
		cout<<ans<<endl;
	}
}