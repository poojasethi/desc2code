#include <bits/stdc++.h>

using namespace std;

#define ll long long int

vector<vector<int> > smoke,mix;
vector<ll> vec;
int calc_smoke(int strt, int end)
{
	if(strt==end)
	{
		mix[strt][end]=vec[strt];
		return 0;
	}
	if(smoke[strt][end]>=0)return smoke[strt][end];
	ll mnsmk=1000000000,mnmx;
	for(int j=strt;j<end;j++)
	{
		ll fs=calc_smoke(strt,j),ss=calc_smoke(j+1,end);
		if(fs+ss+mix[strt][j]*mix[j+1][end]<mnsmk)
		{
			mnsmk=fs+ss+mix[strt][j]*mix[j+1][end];
			mnmx=(mix[strt][j]+mix[j+1][end])%100;
		}
	}
	mix[strt][end]=mnmx;
	smoke[strt][end]=mnsmk;
	return mnsmk;
}


int main()
{
	ll n;
	while(cin>>n)
	{
		
		vec.resize(n+1);
		for(ll i=1;i<=n;i++)
		{
			cin>>vec[i];
		}
		
		mix.resize(n+1);
		smoke.resize(n+1);
		for(int i=0;i<=n;i++)
		{
			smoke[i].resize(n+1);
			mix[i].resize(n+1);
			for(int j=0;j<=n;j++)
			{
				smoke[i][j]=-1;
				mix[i][j]=-1;
			}
		}
		cout<<calc_smoke(1,n)<<endl;
	}
}