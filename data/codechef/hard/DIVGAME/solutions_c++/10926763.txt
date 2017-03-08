#include <bits/stdc++.h>

using namespace std;

vector<int> integers,primes,powers_of_2;

void make_primes()
{
	for(int i=2;i<10005;i++)
	{
		if(integers[i]==1)continue;
		for(int j=2*i;j<10005;j+=i)
		{
			integers[j]=1;
		}
	}
	for(int i=2;i<10005;i++)
	{
		if(integers[i]==0)primes.push_back(i);
	}
}

int main()
{
	integers.resize(10005);
	make_primes();
	int t,n;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		bool isprime=true;
		for(int j=0;j<primes.size()&&primes[j]<n;j++)
		{
			if(n%primes[j]==0){isprime=false;break;}
		}
		
		if((isprime&&n!=2&&n!=17))cout<<"Tom"<<endl;
		else if(n==2||n==17) cout<<"Mike"<<endl;
		else if(n!=16&&n!=34&&n!=289&&!isprime)cout<<"Mike"<<endl;
		else cout<<"Tom"<<endl;
	}
}