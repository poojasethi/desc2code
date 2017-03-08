#include<iostream>
using namespace std;
int n,K,v[200100],A,B;
long long sum[200100],sol;

int main()
{
	int i,maxim;
	cin>>n>>K;
	for(i=1;i<=n;i++)
	{
		cin>>v[i];
		sum[i]=sum[i-1]+1LL*v[i];
	}
	maxim=1;
	for(i=2*K;i<=n;i++)
	{
		if(sum[i-K]-sum[i-2*K]>sum[maxim+K-1]-sum[maxim-1])
			maxim=i-2*K+1;
		if(sum[i]-sum[i-K]+sum[maxim+K-1]-sum[maxim-1]>sol)
		{
			sol=sum[i]-sum[i-K]+sum[maxim+K-1]-sum[maxim-1];
			A=maxim;
			B=i-K+1;
		}
	}
	cout<<A<<' '<<B<<"\n";
	return 0;
}
