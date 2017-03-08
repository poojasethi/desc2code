#include <bits/stdc++.h>
using namespace std ;
long long int num[100000+7];
long long int a[100000+7];
int main()
{
	long long int n ;
	cin >> n ;
	for(long long int i=0;i<n;i++)
	{
		cin >> num[i] ;
	}
	for(long long int i=0;i<n;i++)
	{
		long long int t=min(i,n-1-i);
		if(num[i]-t>0)
		{
			a[num[i]-t]++;
		}
	}
	long long int mx=-1;
	for(long long int i=1;i<100000+7;i++)
	{
		mx=max(mx,a[i]);
	}
	cout << n-mx ;
	return 0;
}