#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>


using namespace std;

#define ll long long int
#define LIM 5000005
#define MOD %1000000007
vector<ll> ans;
vector<ll> num_primes;

void calc_primes()
{
	vector<ll> primes;
	primes.resize(LIM);
	for(int i=2;i<LIM;i++)
	{
		if(primes[i]==1)continue;
		//cout<<i<<" kk"<<endl;
		for(int j=2*i;j<LIM;j+=i)
		{
			//cout<<j<<endl;
			primes[j]=1;
		}
	}
	
	num_primes.resize(LIM);
	
	for(int i=1;i<LIM;i++)
	{
		if(primes[i]==1)num_primes[i]=num_primes[i-1];
		else num_primes[i]=num_primes[i-1]+1;
	}
	return;
}


int main()
{
	calc_primes();
	
	ans.resize(LIM);
	ans[1]=1;
	for(int i=2;i<LIM;i++)
	{
		ans[i]=(ans[i-1]*num_primes[i])MOD;
	}
	int t,var;
	//cin>>t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d",&var);
		printf("%lld\n",ans[var]);
		//cout<<ans[var]<<endl;
	}

}