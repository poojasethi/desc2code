#include <bits/stdc++.h>

using namespace std;
#define ll long long int

vector<ll> vec,primes; 

void makeprimes()
{
	for(int i=2;i<100000;i++)
	{
		if(vec[i]==1)continue;
		primes.push_back(i);
		for(int j=2*i;j<100000;j+=i)
		{
			vec[j]=1;
		}
	}
}

ll tellprimes(ll m, ll n)
{
	vector<ll> temp;
	temp.resize(n-m+1);
	for(int i=0;i<primes.size();i++)
	{
		ll var=m,ver;
		if(m%primes[i]==0)ver=m;
		else ver=(m/primes[i]+1)*primes[i];
		//cout<<ver<<" "<<primes[i]<<endl;
		ver-=m;
		for(int j=max(2*primes[i]-m,ver);j<n-m+1;j+=primes[i])
		{
			temp[j]=1;
		}
	}
	int count=0;
	for(int i=0;i<temp.size();i++)
	{
		if(temp[i]==0&&i+m>1){cout<<i+m<<endl;count++;}
	}
	
	return count;
}

int main()
{
	vec.resize(100000);
	makeprimes();
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		ll m,n;
		cin>>m>>n;
		tellprimes(m,n);
		if(t!=test+1)cout<<endl;
	}
}
