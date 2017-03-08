#include<iostream>
#include<cstdio>
using namespace std;
double a[110],b,sol[110];
int n;

int main()
{
	int i;
	double sum=0.0;
	cin>>n>>b;
	for(i=1;i<=n;i++)
	{
		cin>>a[i];
		sum+=a[i];
	}
	sum+=b;
	sum/=(double)n;
	for(i=1;i<=n;i++)
	{
		sol[i]=sum-a[i];
		if(a[i]>sum)
		{
			cout<<"-1\n";
			return 0;
		}
	}
	for(i=1;i<=n;i++)
	{
		printf("%lf\n",sol[i]);
	}
	return 0;
}
