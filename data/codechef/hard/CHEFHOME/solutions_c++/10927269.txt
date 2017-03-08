#include <bits/stdc++.h>


using namespace std;

#define ll long long int


int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		vector<ll> x,y;
		x.resize(n);
		y.resize(n);
		for(int j=0;j<n;j++)
		{
			cin>>x[j]>>y[j];
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		ll a,b;
		if(n%2==1)
		{
			a=1;
			b=1;
		}
		else
		{
			a=x[n/2]+1-x[n/2-1];
			b=y[n/2]+1-y[n/2-1];
		}
		cout<<a*b<<endl;
	}
}